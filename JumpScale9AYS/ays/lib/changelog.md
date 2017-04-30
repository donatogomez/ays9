# Change logs:

## Version 8.2.0:

### Architecture:
We have unified all the component from the previous version into a single process. Which means now, the AYS librairy, the REST API and the daemon are all running in the same process.
This simplify the deployement of the cockpits and allow to have better performance since there is no interprocess communication.

We moved away from subprocessing for job execution in favor of asyncio.  
The REST API as also been migrated to asyncio. It now use [Sanic](https://github.com/channelcat/sanic) instead of [flask](http://flask.pocoo.org/).

On consequence of AYS becoming a server is that the only way to communicate with it is now through the REST API. The `ays` CLI has been updated to talk to the API instead of directly using the AYS librairy. It can be used as an example of how to implements client application on top of AYS-8.2.0

### API changes:

#### Types:
- new `Actor` type
- update attribute in `Template` type:
    - `schema_hrd` becomes `schema`
    - `actor_hrd` becomes `config`

#### Endpoints:
- ##### deleted endpoints:
  - `/cockpit` doesn't exist anymore

- ##### New endpoints:
  - `/template_repo` : allow you to add new actor template repo
  - `/repository/{repository}/actor` : list actor from an AYS repository
  - `/repository/{repository}/actor/{actor}` : get detail/update about an actor
  - POST `/repository/{repository}/aysrun` : this call doesn't execute the run anymore
  - POST `/repository/{repository}/aysrun/{aysrun}` : this call is used to execute a previously created run
