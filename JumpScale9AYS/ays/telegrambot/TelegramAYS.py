from js9 import j
import telegram
from telegram import Updater
from telegram.ext.dispatcher import run_async
import time
import re
import sys

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='[+][%(levelname)s] %(name)s: %(message)s')


class TelegramAYS:
    #
    # initializing
    #

    def __init__(self, token, rootpath='/opt/code/telegram-projects/'):
        self.token = token
        self.rootpath = rootpath

        print("[+] initializing telegram bot")
        self.updater = Updater(token=self.token)
        self.bot = self.updater.bot
        dispatcher = self.updater.dispatcher

        print("[+] make sure ssh-agent is running")
        if not j.sal.process.checkProcessRunning('ssh-agent'):
            j.sal.process.execute('eval `ssh-agent`')

        # commands
        dispatcher.addTelegramCommandHandler('start', self.start)
        dispatcher.addTelegramCommandHandler('project', self.project)
        dispatcher.addTelegramCommandHandler('blueprint', self.blueprint)
        dispatcher.addTelegramCommandHandler('ays', self.ays)
        dispatcher.addTelegramCommandHandler('help', self.help)

        # messages
        dispatcher.addTelegramMessageHandler(self.message)

        # internal
        dispatcher.addUnknownTelegramCommandHandler(self.unknown)

        print("[+] projects will be saved to: %s" % rootpath)
        j.sal.fs.createDir(rootpath)

        print("[+] loading existing users")
        self.users = self.restore()

    def restore(self):
        usersList = j.sal.fs.listDirsInDir(self.rootpath)
        users = {}

        for user in usersList:
            username = j.sal.fs.getBaseName(user)
            users[username] = {
                'current': None,
                'projects': []
            }

            for project in j.sal.fs.listDirsInDir(user):
                projectName = j.sal.fs.getBaseName(project)
                users[username]['projects'].append(projectName)

        print('[+] users loaded: %s' % users)
        return users

    #
    # local management
    #
    def _setCurrentProject(self, username, project):
        self.users[username]['current'] = project

    def _currentProject(self, username):
        return self.users[username]['current']

    def _getProjects(self, username):
        return self.users[username]['projects']

    def _addProject(self, username, project):
        self.users[username]['projects'].append(project)

    def _projectPath(self, username, project):
        return '%s/%s/%s' % (self.rootpath, username, project)

    def _blueprintsPath(self, username, project):
        return '%s/%s/%s/blueprints' % (self.rootpath, username, project)

    def _currentProjectPath(self, username):
        return self._projectPath(username, self._currentProject(username))

    def _currentBlueprintsPath(self, username):
        return self._blueprintsPath(username, self._currentProject(username))

    #
    # helpers
    #
    def executeProgressive(self, bot, update, command):
        print("[+] executing: %s" % command)
        process = j.sal.process.execute(command, showout=False,
                               useShell=False, die=False, async=True)

        prefixs = ['INIT:', 'RUN:', 'NO METHODS FOR:', 'OUT:', 'Exception:']

        rawbuffer = []
        outbuffer = []
        lasttime = time.time()

        while True:
            line = process.stdout.readline()
            if line == '':
                break

            sys.stdout.write("[+] ays instance: %s" % line)
            rawbuffer.append(line)

            for prefix in prefixs:
                if line.startswith(prefix):
                    outbuffer.append(line)

            # flush each seconde
            if time.time() > lasttime + 1:
                self.bulkSend(bot, update, "\n".join(outbuffer))
                outbuffer = []
                lasttime = time.time()

        self.bulkSend(bot, update, "".join(outbuffer))
        outbuffer = []

        while True:
            line = process.stderr.readline()

            if line == '':
                if len(outbuffer) > 0:
                    bot.sendMessage(chat_id=update.message.chat_id,
                                    text="Sorry, I saw these errors during the execution:")
                    self.bulkSend(bot, update, "".join(outbuffer))

                break

            else:
                outbuffer.append(line)

        bot.sendMessage(chat_id=update.message.chat_id, text="I'm done.")

    def bulkSend(self, bot, update, message):
        buffer = message

        if buffer == "":
            print("[-] nothing to send")
            return

        # checking if not too long limit is set to 4096 UTF-8 bytes
        if len(buffer) > 3840:
            print('[-] buffer too long, chunking...')

            content = message.split("\n")
            buffer = ""

            for chunk in content:
                # append to buffer if it fit
                if len(chunk) + len(buffer) < 3840:
                    buffer += ("%s\n" % chunk)

                # not fit, sending current buffer then creating a new one
                else:
                    bot.sendMessage(chat_id=update.message.chat_id,
                                    text="```\n%s\n```" % buffer, parse_mode="Markdown")
                    buffer = chunk

        # chunked or not, we send buffer, if chunked, buffer will contains last
        # chunk
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="```\n%s\n```" % buffer, parse_mode="Markdown")

    #
    # repositories manager
    #
    def _initRepo(self, username, project):
        repopath = '%s/%s/%s' % (self.rootpath, username, project)
        print('[+] initializing repository: %s' % repopath)

        j.sal.fs.createDir(repopath)
        j.sal.fs.createDir('%s/blueprints' % repopath)
        j.sal.fs.writeFile('%s/.ays' % repopath, '')

        previous = j.sal.fs.getcwd()
        j.sal.fs.changeDir(repopath)

        # initialize empty git repository
        j.sal.process.execute("git init", showout=False, die=False)

        j.sal.fs.changeDir(previous)

    def _userCheck(self, bot, update):
        if not self.users.get(update.message.from_user.username):
            bot.sendMessage(chat_id=update.message.chat_id,
                            text='Hello buddy, please use /start at first.')
            return False

        return True

    def _projectsList(self, bot, update):
        print('[+] listing projects')
        username = update.message.from_user.username
        chatid = update.message.chat_id

        # current project (working on)
        if not self._currentProject(username):
            bot.sendMessage(chat_id=chatid, text="No project selected now.")

        else:
            bot.sendMessage(chat_id=chatid, text="Current project: %s" %
                            self._currentProject(username))

        # projects list
        if len(self._getProjects(username)) == 0:
            message = "You don't have any project for now, create the first one with: `/project [name]`"
            return bot.sendMessage(chat_id=chatid, text=message, parse_mode="Markdown")

        ln = len(self._getProjects(username))
        projectsList = ["I have %d project%s for you:" %
                        (ln, "s" if ln > 1 else "")]

        for project in self._getProjects(username):
            projectsList.append(" - %s" % project)

        bot.sendMessage(chat_id=chatid, text="\n".join(projectsList))

    def _projectsDelete(self, bot, update, projects):
        print('[+] deleting projects: %s' % projects)

        username = update.message.from_user.username
        chatid = update.message.chat_id

        for project in projects:
            if project not in self._getProjects(username):
                message = "Sorry, I can't find any project named `%s` :/" % project
                bot.sendMessage(chat_id=chatid, text=message,
                                parse_mode="Markdown")
                continue

            if project == self._currentProject(username):
                self._setCurrentProject(username, None)

            local = self._projectPath(username, project)

            print('[+] removing repository: %s' % local)
            j.sal.fs.removeDirTree(local)
            self.users[username]['projects'].remove(project)

            message = "Project `%s` removed" % project
            bot.sendMessage(chat_id=chatid, text=message,
                            parse_mode="Markdown")

    def _projectsCheckout(self, bot, update, project):
        print('[+] checking out project: %s' % project)

        username = update.message.from_user.username
        chatid = update.message.chat_id

        # check project name validity
        p = re.compile(r'^[a-zA-Z0-9-_]+$')
        if not re.search(p, project):
            message = "Sorry, I don't support this project name, please name it without any special characters or spaces."
            return bot.sendMessage(chat_id=chatid, text=message)

        # project already exists
        if project in self._getProjects(username):
            self._setCurrentProject(username, project)

            message = "This project already exists, `%s` is now your current working project." % project
            return bot.sendMessage(chat_id=chatid, text=message, parse_mode="Markdown")

        # creating new project
        self._initRepo(username, project)
        self._setCurrentProject(username, project)
        self._addProject(username, project)

        message = "Project `%s` created, it's now your current working project." % project
        bot.sendMessage(chat_id=chatid, text=message, parse_mode="Markdown")

    def _blueprintsList(self, bot, update, project):
        username = update.message.from_user.username
        blueprints = j.sal.fs.listFilesInDir(
            self._currentBlueprintsPath(username))

        bluelist = ["Blueprints for [%s]:" % project]
        for bluepath in blueprints:
            blueprint = j.sal.fs.getBaseName(bluepath)
            bluelist.append(' - %s' % blueprint)

        if len(bluelist) == 1:
            bluelist = [
                "Sorry, this repository doesn't contains blueprint for now, upload me some of them !"]

        bot.sendMessage(chat_id=update.message.chat_id,
                        text="\n".join(bluelist))

    def _blueprintsDelete(self, bot, update, project, names):
        username = update.message.from_user.username

        # ays uninstall before
        self._ays_sync(bot, update, args=['do', 'uninstall'])
        j.actions.resetAll()

        for name in names:
            if name == "*" or name == "all":
                blueprints = j.sal.fs.listFilesInDir(
                    self._currentBlueprintsPath(username))
                for blueprint in blueprints:
                    j.sal.fs.remove(blueprint)

                ln = len(blueprints)
                message = "%d blueprint%s removed" % (
                    ln, "s" if ln > 1 else "")
                bot.sendMessage(chat_id=update.message.chat_id, text=message)

            else:
                blueprint = '%s/%s' % (self._blueprintsPath(username,
                                                            project), name)

                print('[+] deleting: %s' % blueprint)

                if not j.sal.fs.exists(blueprint):
                    message = "Sorry, I don't find any blueprint named `%s`, you can list them with `/blueprint`" % name
                    bot.sendMessage(chat_id=update.message.chat_id,
                                    text=message, parse_mode="Markdown")
                    continue

                j.sal.fs.remove(blueprint)

                message = "Blueprint `%s` removed from `%s`" % (name, project)
                bot.sendMessage(chat_id=update.message.chat_id,
                                text=message, parse_mode="Markdown")

        # cleaning
        j.sal.fs.removeDirTree('%s/alog' % self._currentProjectPath(username))
        j.sal.fs.removeDirTree('%s/actors' %
                               self._currentProjectPath(username))
        j.sal.fs.removeDirTree('%s/services' %
                               self._currentProjectPath(username))
        j.sal.fs.createDir('%s/services' % self._currentProjectPath(username))

    def _blueprintsDeletePrompt(self, bot, update, project):
        username = update.message.from_user.username
        blueprints = j.sal.fs.listFilesInDir(
            self._currentBlueprintsPath(username))

        bluelist = []

        for bluepath in blueprints:
            blueprint = j.sal.fs.getBaseName(bluepath)
            bluelist.append('/blueprint delete %s' % blueprint)

        if len(bluelist) == 0:
            return bot.sendMessage(chat_id=update.message.chat_id,
                                   text="Sorry, this repository doesn't contains blueprint for now, upload me some of them !")

        bluelist.append("I'm done")

        custom_keyboard = [bluelist]
        reply_markup = telegram.ReplyKeyboardMarkup(
            custom_keyboard, resize_keyboard=True)
        return bot.sendMessage(chat_id=update.message.chat_id, text="Which blueprint do you want to delete ?", reply_markup=reply_markup)

    def _blueprintGetAll(self, bot, update, project):
        files = j.sal.fs.listFilesInDir(
            self._blueprintsPath(username, project))
        print("[+] blueprints: %s" % files)

        for file in files:
            name = j.sal.fs.getBaseName(file)
            self._blueprintGet(bot, update, name, project)

    def _blueprintGet(self, bot, update, name, project):
        username = update.message.from_user.username
        blueprint = '%s/%s' % (self._blueprintsPath(username, project), name)

        print('[+] grabbing: %s' % blueprint)

        if not j.sal.fs.exists(blueprint):
            message = "Sorry, I don't find this blueprint, you can list them with `/blueprint`"
            return bot.sendMessage(chat_id=update.message.chat_id, text=message, parse_mode="Markdown")

        content = j.sal.fs.fileGetContents(blueprint)
        self.bulkSend(bot, update, content)

    #
    # messages handlers
    #
    def document(self, bot, update):
        username = update.message.from_user.username
        doc = update.message.document
        item = bot.getFile(doc.file_id)
        local = '%s/%s' % (self._currentBlueprintsPath(username),
                           doc.file_name)

        if not self._currentProject(username):
            message = "Sorry, you are not working on a project currently, use `/project [name]` to create a new one"
            return bot.sendMessage(chat_id=update.message.chat_id, text=message, parse_mode="Markdown")

        if j.sal.fs.exists(local):
            j.sal.fs.remove(local)

        print("[+] document: %s -> %s" % (item.file_path, local))
        j.sal.nettools.download(item.file_path, local)

        bot.sendMessage(chat_id=update.message.chat_id,
                        text="File received: %s" % doc.file_name)

    def project(self, bot, update, args):
        print('[+] project management for: %s' %
              update.message.from_user.username)
        if not self._userCheck(bot, update):
            return

        # no arguments
        if len(args) == 0:
            return self._projectsList(bot, update)

        # projects list
        if args[0] == "list":
            return self._projectsList(bot, update)

        # projects delete
        if (args[0] == "delete" or args[0] == "remove") and len(args) == 1:
            return bot.sendMessage(chat_id=update.message.chat_id, text="Ehm, need to give me a project name")

        if (args[0] == "delete" or args[0] == "remove") and len(args) > 1:
            args.pop(0)
            return self._projectsDelete(bot, update, args)

        # creating project
        return self._projectsCheckout(bot, update, args[0])

    def blueprint(self, bot, update, args):
        username = update.message.from_user.username

        print('[+] blueprint management for: %s' % username)
        if not self._userCheck(bot, update):
            return

        if not self._currentProject(username):
            message = "Sorry, you are not working on a project currently, use `/project [name]` to create a new one"
            return bot.sendMessage(chat_id=update.message.chat_id, text=message, parse_mode="Markdown")

        # no arguments
        if len(args) == 0:
            return self._blueprintsList(bot, update, self._currentProject(username))

        # list blueprints
        if args[0] == "list":
            return self._blueprintsList(bot, update, self._currentProject(username))

        # delete a blueprints
        if (args[0] == "delete" or args[0] == "remove") and len(args) == 1:
            # return bot.sendMessage(chat_id=update.message.chat_id, text="Ehm, need to give me a blueprint name")
            # keyboard
            return self._blueprintsDeletePrompt(bot, update, self._currentProject(username))

        if (args[0] == "delete" or args[0] == "remove") and len(args) > 1:
            args.pop(0)
            return self._blueprintsDelete(bot, update, self._currentProject(username), args)

        if args[0] == "all":
            return self._blueprintGetAll(bot, update, self._currentProject(username))

        # retreive blueprint
        return self._blueprintGet(bot, update, args[0], self._currentProject(username))

    def _ays_sync(self, bot, update, args):
        username = update.message.from_user.username

        print('[+] ays commands for: %s' % username)
        if not self._userCheck(bot, update):
            return

        if not self._currentProject(username):
            message = "Sorry, you are not working on a project currently, use `/project [name]` to create a new one"
            return bot.sendMessage(chat_id=update.message.chat_id, text=message, parse_mode="Markdown")

        repopath = self._currentBlueprintsPath(username)

        previous = j.sal.fs.getcwd()
        j.sal.fs.changeDir(repopath)

        bot.sendMessage(chat_id=update.message.chat_id,
                        text='Executing command...')

        # using list for auto-escape
        ays = 'ays'
        command = [ays] + args

        self.executeProgressive(bot, update, command)
        j.sal.fs.changeDir(previous)

    @run_async
    def ays(self, bot, update, **kwargs):
        return self._ays_sync(bot, update, kwargs['args'])

    @run_async
    def message(self, bot, update, **kwargs):
        username = update.message.from_user.username
        print('[+] %s [%s]: %s' %
              (username, update.message.chat_id, update.message.text))

        if getattr(update.message, 'document', None):
            self.document(bot, update)
            return

        if update.message.text == "I'm done":
            reply_markup = telegram.ReplyKeyboardHide()
            return bot.sendMessage(chat_id=update.message.chat_id, text="Fine", reply_markup=reply_markup)

        # check if it's a blueprint
        try:
            yaml = j.data.serializer.yaml.loads(update.message.text)

            def generate_unique_name():
                name = '%s.yaml' % j.data.time.getLocalTimeHRForFilesystem()
                path = '%s/%s' % (self._currentBlueprintsPath(username), name)
                while j.sal.fs.exists(path):
                    time.sleep(1)
                    name = '%s.yaml' % j.data.time.getLocalTimeHRForFilesystem()
                    path = '%s/%s' % (self._currentBlueprintsPath(username), name)
                return name
            custom = generate_unique_name()

            if not self._currentProject(username):
                message = "You need to create a project before sending me blueprint. See /project"
                return bot.sendMessage(chat_id=update.message.chat_id, text=message)

            # saving blueprint
            local = '%s/%s' % (self._currentBlueprintsPath(username), custom)
            j.sal.fs.writeFile(local, update.message.text)

            message = "This look like a blueprint, I saved it to: %s. Let me initialize it." % custom
            bot.sendMessage(chat_id=update.message.chat_id, text=message)

            return self._ays_sync(bot, update, ["init"])

        except e:
            print(e)
            print("[-] not a blueprint message")
            pass

        message = "Sorry, I can only match on some commands. Try /help to have more help :)"
        # reply_markup = telegram.ReplyKeyboardHide()
        # bot.sendMessage(chat_id=update.message.chat_id, text=message, reply_markup=reply_markup)
        bot.sendMessage(chat_id=update.message.chat_id, text=message)

    def help(self, bot, update):
        message = [
            "*Okay buddy, this is how I work:*",
            "",
            "At first, you need to run `/start` to let me know you.",
            "",
            "After that, you will be able to run some commands:",
            "`/project` - `/blueprint` - `/ays`",
            "",
            "*/project*: let you manage your differents projects (or repository)",
            " - `/project [name]`: will move your current project to `[name]`, if it doesn't exists it will be created",
            " - `/project delete [name]`: will delete the project `[name]`",
            " - `/project list`: will show you your projects list",
            "",
            "When you are ready with your project, simply upload me some blueprint, they will be put on your services repository",
            "",
            "*/blueprint*: will manage the project's blueprints",
            " - `/blueprint list`: will show you your project's blueprint saved",
            " - `/blueprint delete [name]`: will delete the blueprint `[name]`",
            " - `/blueprint delete all`: will delete all the blueprints in your project",
            " - `/blueprint [name]`: will show you the content of the blueprint `[name]`",
            "",
            "When your blueprints are ready, you can go further:",
            "",
            "*/ays*: will control atyourservice",
            " - `/ays init`: will run 'ays init' in your repository",
            " - `/ays do install`: will run 'ays do install' in your repository",
            " - ...",
            "",
            "This message was given by `/help`, have fun with me !",
        ]

        bot.sendMessage(chat_id=update.message.chat_id,
                        text="\n".join(message), parse_mode="Markdown")

    # initialize
    def start(self, bot, update):
        username = update.message.from_user.username

        print("[+] hello from: %s (%s %s) [ID %s]" %
              (username,
               update.message.from_user.first_name,
               update.message.from_user.last_name,
               update.message.chat_id))

        # creating environment for this user
        userpath = '%s/%s' % (self.rootpath, username)

        if not j.sal.fs.exists(userpath):
            j.sal.fs.createDir(userpath)

        if not self.users.get(username):
            hello = "Hello %s !" % update.message.from_user.first_name
            self.users[username] = {'current': None, 'projects': []}

        else:
            hello = "Welcome back %s !" % update.message.from_user.first_name

        message = [
            hello,
            "",
            "Let's start:",
            " - create a project with: `/project [name]`",
            " - upload some blueprints",
            " - do a *ays init* with `/ays init`",
            " - do a *ays [stuff]* with `/ays [stuff]`",
            "",
            "For more information, just type `/help` :)"
        ]

        bot.sendMessage(chat_id=update.message.chat_id,
                        text="\n".join(message), parse_mode="Markdown")

    # project manager
    def unknown(self, bot, update):
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Sorry, I didn't understand that command.")

    #
    # management
    #
    def run(self):
        self.updater.start_polling()
        print("[+] bot is listening")
