# How to Get a JWT

You will need to create an API key in ItsYou.online for a user that has access to the targeted environment.

```bash
CLIENTID="..."
SECRET="..."
curl -d "grant_type=client_credentials&client_id=${CLIENTID}&client_secret=${SECRET}&response_type=id_token" https://itsyou.online/v1/oauth/access_token
```

> Excluding ``&response_type=id_token` will only yield an access token, not a JWT.
