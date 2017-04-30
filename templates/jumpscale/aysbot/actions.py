def install(job):
    service = job.service
    cuisine = job.service.executor.cuisine

    cfg = {'token': service.model.data.botToken,
           'oauth': {
               'host': service.model.data.oauthHost,
               'port': service.model.data.oauthPort,
               'organization': service.model.data.oauthClient,
               'client_id': service.model.data.oauthClient,
               'client_secret': service.model.data.oauthSecret,
               'redirect_uri': service.model.data.oauthRedirect,
               'itsyouonlinehost': service.model.data.oauthItsyouonlinehost
               }
           }
    cuisine.apps.aysbot.create_config(cfg=cfg)
    cuisine.apps.aysbot.install()

def start(job):
    cuisine = job.service.executor.cuisine
    cuisine.processmanager.start('aysbot__main')


def stop(job):
    cuisine = job.service.executor.cuisine
    cuisine.processmanager.stop('aysbot__main')
