# template: caddy

## Description:
This actor template is install and managed a [caddy](caddyserver.com) server.

## Schema:

os: name of the os parent service. **required**

- hostname: hostname caddy should listen on. This can be a valid domain or a IP - address. if it's a valid domain caddy will enable auto SSL feature using let's encrypt. **required**
- gzip: enable or not gzip compression. default to True **required**
- email: email to use for registration on let's encrypt **required**
- stagging: use stagging environement for auto SSL or not. Usefull for developemnt to prevent hitting limit of certificate creation. disable in production. default to false. **required**
- caddy_proxy: a list of caddy_proxy service to consume. each consumed service will create a proxy entry in the configuration. **optional**
