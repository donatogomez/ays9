def install(job):
    service = job.service
    cuisine = service.executor.cuisine

    if 'redis' not in service.producers:
        raise j.exceptions.AYSNotFound("Can't find redis service in producers.")

    # configure redis connection for AYS
    redis = service.producers['redis'][0]
    # this line create the default config if it doesn't exsits yet
    cfg_path = cuisine.core.replace("$JSCFGDIR/jumpscale/ays.yaml")
    config = j.data.serializer.yaml.loads("redis:\n    host: 'localhost'\n    port: 6379\n")
    if cuisine.core.file_exists(cfg_path):
        config = j.data.serializer.yaml.loads(cuisine.core.file_read(cfg_path))
    if 'redis' not in config:
        config['redis'] = {}

    # configure AYS daemon
    if redis.model.data.unixsocket != '':
        config['redis']['unixsocket'] = redis.model.data.unixsocket
    else:
        config['redis'] = {
            'host': redis.model.data.host,
            'port': redis.model.data.port,
        }

    cuisine.core.dir_ensure(j.sal.fs.getParent(cfg_path))
    cuisine.core.file_write(cfg_path, j.data.serializer.yaml.dumps(config))

    # configure REST API
    raml = cuisine.core.file_read('$JSAPPSDIR/ays_api/ays_api/apidocs/api.raml')
    if service.model.data.domain == '':  # if no domain is set use ip instead
        node = service.aysrepo.servicesFind(actor='node.*')[0]
        service.model.data.domain = node.model.data.ipPublic
        raml = raml.replace('$(baseuri)', "http://%s/api" % service.model.data.domain)
    else:
        raml = raml.replace('$(baseuri)', "https://%s/api" % service.model.data.domain)
    cuisine.core.file_write('$JSAPPSDIR/ays_api/ays_api/apidocs/api.raml', raml)
    content = cuisine.core.file_read('$JSAPPSDIR/portals/main/base/AYS81/.space/nav.wiki')
    if 'REST API:/api' not in content:
        cuisine.core.file_write('$JSAPPSDIR/portals/main/base/AYS81/.space/nav.wiki',
                                'REST API:/api',
                                append=True)

    if service.model.data.oauthRedirectUrl.split('/')[2] == '':  # if no domain is set use ip instead
        node = service.aysrepo.servicesFind(actor='node.*')[0]
        redirect_url = service.model.data.oauthRedirectUrl.split('/')
        redirect_url[2] = node.model.data.ipPublic
        #  use http instead of https
        redirect_url[0] = 'http:'
        service.model.data.oauthRedirectUrl = '/'.join(redirect_url)

    api_cfg = {
        'oauth': {
            'client_secret': service.model.data.oauthClientSecret,
            'client_id': service.model.data.oauthClientId,
            'organization': service.model.data.oauthOrganization,
            'jwt_key': service.model.data.oauthJwtKey,
            'redirect_uri': service.model.data.oauthRedirectUrl,
        },
        'api': {
            'ays': {
                'host': service.model.data.apiHost,
                'port': service.model.data.apiPort,
            }
        }
    }
    cuisine.core.file_write('$JSCFGDIR/cockpit_api/config.toml', j.data.serializer.toml.dumps(api_cfg))

    # installed required package
    cuisine.package.mdupdate()
    cuisine.package.install('git')

    # start daemon
    cmd = 'ays start'
    pm = cuisine.processmanager.get('tmux')
    pm.ensure(cmd=cmd, name='cockpit_daemon_%s' % service.name, autostart=True)
    # start api
    cmd = 'jspython api_server'
    pm.ensure(cmd=cmd, name='cockpit_api_%s' % service.name, path=cuisine.core.replace('$JSAPPSDIR/ays_api'), autostart=True)
    # upload the aysrepo used in installing to the cockpit
    cuisine.core.dir_ensure('$VARDIR/cockpit_repos')
    cuisine.core.upload(service.aysrepo.path, '$VARDIR/cockpit_repos/cockpit')
    cuisine.core.run('cd $VARDIR/cockpit_repos/cockpit; ays restore', profile=True)

    # write the init script that will be used in case of machine shutdown
    rc_local = cuisine.core.file_read('/etc/rc.local').split('\n')
    for idx, line in enumerate(rc_local):
        if line == 'exit 0':
            rc_local.insert(idx, 'bash /etc/startup.sh')
            rc_local.insert(idx, 'export HOME=/root')
            break
    cuisine.core.file_write('/etc/rc.local', '\n'.join(rc_local))


def start(job):
    service = job.service
    cuisine = service.executor.cuisine

    pm = cuisine.processmanager.get('tmux')

    cmd = 'ays start'
    pm.ensure(cmd=cmd, name='cockpit_daemon_%s' % service.name)

    # in case we update the sandbox, need to reconfigure the raml with correct url
    raml = cuisine.core.file_read('$JSAPPSDIR/ays_api/ays_api/apidocs/api.raml')
    raml = raml.replace('$(baseuri)', "https://%s/api" % service.model.data.domain)
    cuisine.core.file_write('$JSAPPSDIR/ays_api/ays_api/apidocs/api.raml', raml)
    cmd = 'jspython api_server'
    pm.ensure(cmd=cmd, name='cockpit_api_%s' % service.name, path=cuisine.core.replace('$JSAPPSDIR/ays_api'))


def stop(job):
    service = job.service
    cuisine = service.executor.cuisine
    pm = cuisine.processmanager.get('tmux')
    pm.stop(name='cockpit_api_%s' % service.name)
    pm.stop(name='cockpit_daemon_%s' % service.name)
