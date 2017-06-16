# How to Create a New OpenvCloud User

First step will be to create a user in ItsYou.online, or rather invite the new user to register at ItsYou.online.

Once the user has been registered in ItsYou.online he will be able to login to OpenvCloud. When this users logs in for the first time he will automatically be registered as an OpenvCloud user with group membership to the `user` group. However, because the new user doesn't have any access rights at that stage to any OpenvCloud account, cloud space (VDC) or virtual machine, he'll get an error. At that point you will need to grant the new user access to a virtual datacenter, as documented in [How to Grant User Access to a VDC](..//README.md), and then invite the user to login again.

Alternatively you can explicitly register an ItsYou.online user as a new OpenvCloud user, instead of requiring the user to login. This can be achieved using a `uservdc` blueprint as defined in the AYS template available here: https://github.com/Jumpscale/ays_jumpscale8/tree/8.2.0/templates/ovc/uservdc

- [Blueprint](#blueprint)
- [Values](#values)

<a id="minimal-blueprint"></a>
## Blueprint

```yaml
g8client__{environment}:
  url: '{url}'
  login: '{login}'
  password: '{password}'
  account: '{account}'

uservdc__{username}:
  g8client: '{environment}'
  email: '{email}'
  provider: 'itsyouonline'
  groups:
    - user

actions:
  - action: install   
```

The `g8client__{environment}` section should of course only be included in your blueprint if you didn't yet include it in another blueprint in the same repository.

Strictly spoken you don't need to list any group membership. So you can leave the `groups` section out, but then the user will not get any group membership, and will not be able to login.

<a id="values"></a>
## Values

- `{environment}`: environment name for referencing elsewhere in the same blueprint or other blueprint in the repository
- `{url}`: URL to to the environment, e.g. `gig.demo.greenitglobe.com`
- `{login}`: username on the targeted G8 environment
- `{password}`: password for the username
- `{account}`: name of the OpenvCloud account
- `{username}`: ItsYou.online username of the users that will get created in OpenvCloud
- `{email}`: email addresses of the new users

Also see [How to Delete a User](../Delete_user/README.md)
