# Start the AYS Portal

When using the JS9 Docker container, first make sure your container is joined to a ZeroTier network, as documented in [Join Your ZeroTier Network](zt.md).

In the JumpScale interactive shell ('js9'):
```python
prefab = j.tools.prefab.local
prefab.apps.portal.install()
```

This will install and start the AYS Portal on port 8200: http://<ZeroTier IP Address of the container>:8200/

See `/optvar/cfg/portals/main/config.yaml` for configuring the AYS Portal:

```bash
mongoengine.connection:
    host: 'localhost'
    port: 27017

rootpasswd: 'admin'

ipaddr: '127.0.0.1'
port: '8200'
appdir: '$JSAPPSDIR/portals/portalbase'
filesroot: '$VARDIR/portal/files'
defaultspace: 'system'
admingroups:
    - 'admin'
authentication.method: 'me'
gitlab.connection: 'main'
force_oauth_instance: ''  # set to use oauth
contentdirs:  ''

production:  False

oauth.client_url:  'https://itsyou.online/v1/oauth/authorize'
oauth.token_url:  'https://itsyou.online/v1/oauth/access_token'
oauth.redirect_url:  'http://ae5d255c.ngrok.io/restmachine/system/oauth/authorize'
oauth.client_scope:  'user:email:main,user:memberof:JSPortal'
oauth.client_id:  'JSPortal'
oauth.client_secret:  '***'
oauth.client_user_info_url:  'https://itsyou.online/api/users/'
oauth.client_logout_url:  ''
oauth.organization: testOrg
oauth.default_groups:
    - admin
    - user
```
