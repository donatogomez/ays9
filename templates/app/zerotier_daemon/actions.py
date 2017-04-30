def install(job):
    """
    Installing zerotier
    """
    service = job.service
    cuisine = service.parent.executor.cuisine

    # build and install zerotier
    cuisine.package.update()
    zerotier_client = cuisine.apps.zerotier
    zerotier_client.build()
    zerotier_client.install()
    zerotier_client.start()
    for network in service.producers['network']:
        zerotier_client.join_network(network.model.data.id)
