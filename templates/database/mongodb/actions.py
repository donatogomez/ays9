def install(job):
    cuisine = job.service.executor.cuisine
    name = 'mongod_%s' % job.service.name
    cuisine.apps.mongodb.install(start=True, name=name)


def start(job):
    cuisine = job.service.executor.cuisine
    name = 'mongod_%s' % job.service.name
    cuisine.apps.mongodb.start(name)


def stop(job):
    cuisine = job.service.executor.cuisine
    name = 'mongod_%s' % job.service.name
    cuisine.apps.mongodb.stop(name)
