# How to Execute Blueprints

Executing a blueprint means that you will initialize all service instances as described in the blueprint.

You can execute a blueprint in three ways:

- [At the CLI](#cli)
- [Using the AYS RESTful API](#rest)
- [In the AYS Portal](#portal)


<a id="cli"></a>
## At the CLI

Once you've created a new AYS repository, as documented in [How to Create a New Repository](../Create_repository/Create_repository.md), a new directory will have been created that contains two empty subdirectories:
- `blueprints`
- `actorTemplates`

```
REPO_NAME="..."
cd $REPO_NAME
```

In order to execute a blueprint, you first need to create the blueprint, as documented in [How to Create Blueprints](../Create_blueprint/Create_blueprint.md).



Once you add your first blueprint, and execute it, two more directories will be created:

- `actors` containing the actor template files:
  - `actions.py`: Python code implementing the actions
  - `actor.json`: template for the AYS service state of each action
  - `schema.capnp`: schema of the AYS service
- `services` containing the actual state (files) for each AYS service (in a subdirectory):
  - `data.json`: information of the AYS service, as set through the blueprint
  - `schema.capnp`: schema of the AYS service
  - `service.json`: the state of each of the actions



<a id="rest"></a>
## Using the AYS RESTful API

In order to use the AYS RESTful API you first need to obtain an JWT, as documented in the section about [how to get a JWT](../Get_JWT/Get_JWT.md).

Once you got the JWT, you can execute a blueprint:

```
curl -H "Authorization: bearer JWT"  /  
     https://BASE_URL/api/ays/repository/REPOSITORY-NAME/blueprint/BLUEPRINT-NAME
```

For instance in order to execute the blueprint discussed in the section [How to create a blueprint](../Create_blueprint/Create_blueprint.md):

```
curl -H "Authorization: bearer JWT"  /  
     https://BASE_URL/api/ays/repository/REPOSITORY-NAME/blueprint/user1.yaml
```

> Note that once executed the user still is not created. One more step is required, that is executing the install action on the user1 service instance, as documented in the section [How to install a service](Install_service/Install_service.md).

Also see the section about the [API Console](../../API_Console/API_Console.md)



<a id="portal"></a>
## Using the AYS Portal

See the [Getting started with blueprints](../../Getting_started_with_blueprints/Getting_started_with_blueprints.md) section.
