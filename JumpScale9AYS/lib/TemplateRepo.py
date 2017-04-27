from js9 import j
from JumpScale.baselib.atyourservice81.lib.ActorTemplate import ActorTemplate
import asyncio


def searchActorTemplates(path, is_global=False):
    """
    walk function that look recursively into 'path' after actor templates directories
    @returns: list of paths of directories containing actor tempaltes
    """
    path = j.sal.fs.pathNormalize(path)

    res = []

    # check if this is already an actortemplate dir, if not no need to recurse
    def isValidTemplate(path):
        dirname = j.sal.fs.getBaseName(path)
        tocheck = ['config.yaml', "schema.capnp", 'actions.py']
        if dirname.startswith("_") or dirname.startswith("."):
            return False
        for aysfile in tocheck:
            if j.sal.fs.exists('%s/%s' % (path, aysfile)):
                if not dirname.startswith("_"):
                    return True
                else:
                    return False
        return False

    def callbackFunctionDir(path, arg):
        if arg[3] != "" and isValidTemplate(path):
            arg[1].append(path)

    def callbackForMatchDir(path, arg):
        base = j.sal.fs.getBaseName(path)
        if base.startswith("."):
            return False
        if base.startswith("ays_"):
            arg[2] = path
        elif arg[2] != "":
            if not path.startswith(arg[2]):
                arg[2] = ""
                # because means that ays repo is no longer our parent

        locations = ["templates", "tests"]
        if not is_global:
            locations.append("actorTemplates")
        if base in locations:
            arg[3] = path
        elif arg[3] != "":
            if not path.startswith(arg[3]):
                arg[3] = ""
                # because means that  is no longer our parent

        depth = len(j.sal.fs.pathRemoveDirPart(path, arg[0]).split("/"))
        if depth < 4:
            return True
        elif depth < 8 and arg[3] != "":
            return True
        return False

    j.sal.fswalker.walkFunctional(path, callbackFunctionFile=None, callbackFunctionDir=callbackFunctionDir, arg=[path, res, "", ""],
                                  callbackForMatchDir=callbackForMatchDir, callbackForMatchFile=lambda x, y: False)
    return res


class TemplateRepoCollection:
    """
    Class reponsible for search/load tempates repos
    """

    def __init__(self):
        self.logger = j.logger.get('j.atyourservice')
        self._loop = asyncio.get_event_loop()  # TODO: question why do we need this
        self._template_repos = {}
        self._load()

    def _load(self):
        self.logger.info("reload actor templates repos")
        for path in searchActorTemplates(j.dirs.CODEDIR, is_global=True):
            self.create(path=path)

        for repo in list(self._template_repos.values()):
            if not j.sal.fs.exists(repo.path):
                self.logger.info("actor template repo {} doesn't exists anymore, unload".format(repo.path))
                del(self._template_repos[repo.path])

        self._loop.call_later(60, self._load)

    def list(self):
        # todo protect with lock
        return list(self._template_repos.values())

    def create(self, path, is_global=True):
        """
        path can be any path in a git repo
        will look for the directory with .git and create a TemplateRepo object if it doesn't exist yet
        """
        original_path = path

        while not j.sal.fs.exists(j.sal.fs.joinPaths(path, ".git")) and path != "":
            path = j.sal.fs.getParent(path).rstrip("/").strip()

        if path not in self._template_repos:
            if path == "":
                # did not find a git parent
                raise j.exceptions.NotFound("path '{}' and its parents is not a git repository".format(original_path))

            self.logger.debug("New template repos found at {}".format(path))
            self._template_repos[path] = TemplateRepo(path, is_global=is_global)

        return self._template_repos[path]

    # TEMPLATES
    # def actorTemplatesUpdate(self):
    #
    #     from IPython import embed
    #     print("DEBUG NOW 9898")
    #     embed()
    #     raise RuntimeError("stop debug here")
    #
    #     repos_path = (root for root, dirs, files in os.walk(path, followlinks=False) if '.ays' in files)
    #
    #     from IPython import embed
    #     print("DEBUG NOW 98989")
    #     embed()
    #     raise RuntimeError("stop debug here")
    #
    #     localGitRepos = j.clients.git.getGitReposListLocal()
    #
    #     # see if all specified ays templateRepo's are downloaded
    #     # if we don't have write permission on /opt don't try do download service templates
    #     codeDir = j.tools.path.get(j.dirs.CODEDIR)
    #     if codeDir.access(os.W_OK):
    #         # can access the opt dir, lets update the atyourservice
    #         # metadata
    #
    #         global_templates_repos = j.atyourservice.config['metadata']
    #
    #         for domain, info in global_templates_repos.items():
    #             url = info['url']
    #             if url.strip() == "":
    #                 raise j.exceptions.RuntimeError("url cannot be empty")
    #         branch = info.get('branch', 'master')
    #         templateReponame = url.rpartition("/")[-1]
    #         if templateReponame not in list(localGitRepos.keys()):
    #             j.do.pullGitRepo(url, dest=None, depth=1, ignorelocalchanges=False, reset=False, branch=branch)

    # def actorTemplatesUpdate(self, templateRepos):
    #     """
    #     update the git templateRepo that contains the service templates
    #     args:
    #         templateRepos : list of dict of templateRepos to update, if empty, all templateRepos are updated
    #                 {
    #                     'url' : 'http://github.com/account/templateRepo',
    #                     'branch' : 'master'
    #                 },
    #                 {
    #                     'url' : 'http://github.com/account/templateRepo',
    #                     'tag' : 'atag'
    #                 },
    #
    #     """
    #     for item in templateRepos:
    #         if 'branch' in item:
    #             branch = item["branch"]
    #         else:
    #             branch = "master"
    #         if 'tag' in item:
    #             tag = item["tag"]
    #         else:
    #             tag = ""
    #
    #         self.actorTemplateAdd(item["url"], branch=branch, tag=tag)
    #         j.do.pullGitRepo(url=templateRepo['url'], branch=branch, tag=tag)
    #
    #     self.reset()

    # @property
    # def actorTemplatesRepos(self):
    #     """
    #     find ays repos
    #     """
    #     if self._actorTemplatesRepos == {}:
    #         self.actorTemplates
    #     return self._actorTemplatesRepos


class TemplateRepo():
    """
    Represent git repository containing Actor templates
    """

    def __init__(self, path, is_global=True):
        self.logger = j.logger.get('j.atyourservice')
        self._loop = asyncio.get_event_loop()
        self.path = j.sal.fs.pathNormalize(path)
        self.git = j.clients.git.get(self.path, check_path=False)
        self.is_global = is_global
        self._templates = {}
        self._load()

    def _load(self):
        """
        path is absolute path (if specified)
        load the actor template in memory
        """
        self.logger.info("reload actor templates from {}".format(self.path))
        for path in searchActorTemplates(self.path, is_global=self.is_global):
            if not j.sal.fs.exists(path=path):
                raise j.exceptions.NotFound("Cannot find path for ays templates:%s" % path)

            templ = ActorTemplate(path=path, template_repo=self)
            if templ.name in self._templates:
                if path != self._templates[templ.name].path:
                    msg = 'Found duplicate template:found %s in \n- %s and \n- %s' % (
                        templ.name, path, self._templates[templ.name].path)
                    raise j.exceptions.Input(msg)

            # self.logger.debug("load template {} from {}".format(templ, path))
            self._templates[templ.name] = templ

        # make sure all loaded repo still exists
        for template in list(self._templates.values()):
            if not j.sal.fs.exists(template.path):
                self.logger.info("template {} doesnt exists anymore, unload".format(template))
                del(self._templates[template.name])

        self._loop.call_later(60, self._load)

    @property
    def templates(self):
        return list(self._templates.values())

    def find(self, name="", domain="", role=''):
        res = []
        for template in self._templates.values():
            if not(name == "" or template.name == name):
                # no match continue
                continue
            if not(domain == "" or template.domain == domain):
                # no match continue
                continue
            if not (role == '' or template.role == role):
                # no match continue
                continue
            res.append(template)
        return res

    def __str__(self):
        return "actor template repo: {}".format(self.path)

    def __repr__(self):
        return self.__str__()
