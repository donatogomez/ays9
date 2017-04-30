def init_actions_(service, args):
    """
    this needs to returns an array of actions representing the depencies between actions.
    Looks at ACTION_DEPS in this module for an example of what is expected
    """
    return {
        'test': ['install']
    }


def test(job):
    import sys
    import time
    try:
        from ast import literal_eval
        log = j.logger.get('test')
        log.addHandler(j.logger._LoggerFactory__fileRotateHandler('tests'))
        service = job.service
        branch = service.model.data.branch
        cuisine = service.executor.cuisine
        log.info('Installing jumpscale on the VM')
        cuisine.core.run('apt-get update')
        cuisine.core.run('echo Y | apt-get install curl')
        cuisine.core.run('curl -k https://raw.githubusercontent.com/Jumpscale/'
                         'jumpscale_core8/{}/install/install.sh > install.sh'.format(branch))
        if branch != "master":
            cuisine.core.run('bash install.sh', env={'JSBRANCH': branch})
        else:
            cuisine.core.run('bash install.sh')
        time.sleep(50)

        log.info('Check if js is working, should succeed')
        output = cuisine.core.run('js "print(j.sal.fs.getcwd())"')
        if output[1] != '/root':
            service.model.data.result = 'FAILED : {} {}'.format('test_js8_install', str(sys.exc_info()[:2]))
            service.save()
            return

        log.info('Making sure Redis started correctly')
        tmpdir = cuisine.core.replace('$TMPDIR')
        output = cuisine.core.run('''js "print(j.core.db.config_get('unixsocket')['unixsocket'])"''')
        sock = '%s/redis.sock' % tmpdir
        if output[1] != sock:
            service.model.data.result = 'FAILED : {} wrong unix socket'.format('test_js8_install')
            service.save()
            return

        log.info('Checking if AYS is usable')
        cuisine.core.execute_bash('ays start')
        output = cuisine.core.run('netstat -nltp')
        if '127.0.0.1:5000' not in output[1]:
            service.model.data.result = 'FAILED : {} AYS not started'.format('test_js8_install')
            service.save()
            return

        log.info('Check if directories under /optvar/ is as expected')
        output = cuisine.core.run('ls /optvar')
        if 'cfg\ndata' not in output[1]:
            service.model.data.result = 'FAILED : {} {}'.format('test_js8_install', str(sys.exc_info()[:2]))
            service.save()
            return

        log.info('Check if directories under /opt/jumpscale8/ is as expected')
        output = cuisine.core.run('ls /opt/jumpscale8/')
        if 'bin\nenv.sh\nlib' not in output[1]:
            service.model.data.result = 'FAILED : {} {}'.format('test_js8_install', str(sys.exc_info()[:2]))
            service.save()
            return

        log.info('Compare js.dir to j.tools.cuisine.local.core.dir_paths, should be the same')
        output = cuisine.core.run('js "print(j.dirs)"')
        output2 = cuisine.core.run('js "print(j.tools.cuisine.local.core.dir_paths)"')

        str_list = output[1].split('\n')
        # remove empty strings found in a list
        for i in str_list:
            var = "".join(i.split())
            str_list[str_list.index(i)] = var.split(':')
        dict1 = dict(str_list)
        dict2 = literal_eval(output2[1])

        log.info('Compare js.dir to j.tools.cuisine.local.core.dir_paths, should be the same')
        output = cuisine.core.run('js "print(j.dirs)"')
        output2 = cuisine.core.run('js "print(j.tools.cuisine.local.core.dir_paths)"')
        str_list = output[1].split('\n')
        # remove empty strings found in a list
        for i in str_list:
            var = "".join(i.split())
            str_list[str_list.index(i)] = var.split(':')
        dict1 = dict(str_list)
        dict2 = literal_eval(output2[1])
        import unittest
        tc = unittest.TestCase()
        tc.assertEqual(dict1['HOMEDIR'], dict2['HOMEDIR'])
        tc.assertEqual(dict1['BASEDIR'], dict2['BASEDIR'])
        tc.assertEqual(dict1['JSAPPSDIR'].replace('/', ''), dict2['JSAPPSDIR'].replace('/', ''))
        tc.assertEqual(dict1['LIBDIR'].replace('/', ''), dict2['LIBDIR'].replace('/', ''))
        tc.assertEqual(dict1['BINDIR'].replace('/', ''), dict2['BINDIR'].replace('/', ''))
        tc.assertEqual(dict1['JSCFGDIR'].replace('/', ''), dict2['JSCFGDIR'].replace('/', ''))
        tc.assertEqual(dict1['CODEDIR'].replace('/', ''), dict2['CODEDIR'].replace('/', ''))
        tc.assertEqual(dict1['JSLIBDIR'].replace('/', ''), dict2['JSLIBDIR'].replace('/', ''))
        tc.assertEqual(dict1['PIDDIR'].replace('/', ''), dict2['PIDDIR'].replace('/', ''))
        tc.assertEqual(dict1['LOGDIR'].replace('/', ''), dict2['LOGDIR'].replace('/', ''))
        tc.assertEqual(dict1['VARDIR'].replace('/', ''), dict2['VARDIR'].replace('/', ''))
        tc.assertEqual(dict1['TEMPLATEDIR'].replace('/', ''), dict2['TEMPLATEDIR'].replace('/', ''))

        log.info('Checking portal installation')
        cuisine.core.run('js "j.tools.cuisine.local.apps.portal.install()"')
        cuisine.core.run('js "j.tools.cuisine.local.apps.portal.start()"')
        output = cuisine.core.run('netstat -nltp')
        if ':8200' not in output[1]:
            service.model.data.result = 'FAILED : {} Portal not started'.format('test_js8_install')
            service.save()
            return
    except:
        service.model.data.result = 'ERROR : {} {}'.format('test_js8_install', str(sys.exc_info()[:2]))
        raise j.exceptions.JSBUG("Error in installation")
    log.info('Test Ended')
    service.save()
