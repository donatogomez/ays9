def install(job):
    """
    Installing owncloud
    """
    service = job.service
    cuisine = service.executor.cuisine

    sitename = service.model.data.sitename
    owncloudAdminUser = service.model.data.owncloudAdminUser
    owncloudAdminPassword = service.model.data.owncloudAdminPassword
    # TODO: **2 add lipaprutil as a work around for apache and php needs to be bundled in the flist
    C = "apt-get update && apt-get install -y python3-mysqldb mysql-client-core-5.7 libaprutil1-dev libapr1-dev"
    cuisine.core.run(C)
    C = "apt-get install -y libzip4 libpng12-0 libxml2 libcurl3 libxslt1.1 libgd3 libgeoip1"
    cuisine.core.run(C)
    cuisine.core.dir_ensure("/var/log/nginx")
    cuisine.core.dir_ensure("/var/lib/nginx")


    tidb = service.producers['tidb'][0]
    tidbos = tidb.parent
    tidbdocker = tidbos.parent
    tidbhost = tidbdocker.model.data.ipPrivate

    tidbuser = service.model.data.tidbuser
    tidbpassword = service.model.data.tidbpassword
    # dbhost=tidb.model.data.dbhost
    # dbuser=tidb.model.data.dbuser
    # dbpass=tidb.model.data.dbpass

    #cuisine.apps.owncloud.install(start=False)
    cuisine.apps.owncloud.start(sitename=sitename, dbhost=tidbhost, dbuser=tidbuser, dbpass=tidbpassword)
