class AysService:
    def __init__(self, client):
        self.client = client



    def reload(self, data, headers=None, query_params=None):
        """
        reload AYS
        It is method for POST /ays/reload
        """
        uri = self.client.base_url + "/ays/reload"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def listRepositories(self, headers=None, query_params=None):
        """
        list all repositorys
        It is method for GET /ays/repository
        """
        uri = self.client.base_url + "/ays/repository"
        return self.client.get(uri, headers=headers, params=query_params)


    def createRepository(self, data, headers=None, query_params=None):
        """
        create a new repository
        It is method for POST /ays/repository
        """
        uri = self.client.base_url + "/ays/repository"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def deleteRepository(self, repository, headers=None, query_params=None):
        """
        Delete a repository
        It is method for DELETE /ays/repository/{repository}
        """
        uri = self.client.base_url + "/ays/repository/"+repository
        return self.client.session.delete(uri, headers=headers, params=query_params)


    def getRepository(self, repository, headers=None, query_params=None):
        """
        Get information of a repository
        It is method for GET /ays/repository/{repository}
        """
        uri = self.client.base_url + "/ays/repository/"+repository
        return self.client.get(uri, headers=headers, params=query_params)


    def listActors(self, repository, headers=None, query_params=None):
        """
        list all actors in the repository
        It is method for GET /ays/repository/{repository}/actor
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/actor"
        return self.client.get(uri, headers=headers, params=query_params)


    def getActorByName(self, actor, repository, headers=None, query_params=None):
        """
        Get an actor by name
        It is method for GET /ays/repository/{repository}/actor/{actor}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/actor/"+actor
        return self.client.get(uri, headers=headers, params=query_params)


    def updateActor(self, data, actor, repository, headers=None, query_params=None):
        """
        update an actor from a template to the last version
        It is method for PUT /ays/repository/{repository}/actor/{actor}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/actor/"+actor
        return self.client.put(uri, data, headers=headers, params=query_params)


    def listRuns(self, repository, headers=None, query_params=None):
        """
        list all runs of the repository
        It is method for GET /ays/repository/{repository}/aysrun
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/aysrun"
        return self.client.get(uri, headers=headers, params=query_params)


    def createRun(self, data, repository, headers=None, query_params=None):
        """
        Create a run based on all the action scheduled. This call returns an AYSRun object describing what is going to hapen on the repository.
        This is an asyncronous call. To be notify of the status of the run when then execution is finised or when an error occurs, you need to specify a callback url.
        A post request will be send to this callback url with the status of the run and the key of the run. Using this key you can inspect in detail the result of the run
        using the 'GET /ays/repository/{repository}/aysrun/{aysrun_key}' endpoint
        It is method for POST /ays/repository/{repository}/aysrun
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/aysrun"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def deleteRun(self, runid, repository, headers=None, query_params=None):
        """
        delete a run
        It is method for DELETE /ays/repository/{repository}/aysrun/{runid}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/aysrun/"+runid
        return self.client.session.delete(uri, headers=headers, params=query_params)


    def getRun(self, runid, repository, headers=None, query_params=None):
        """
        Get an aysrun
        It is method for GET /ays/repository/{repository}/aysrun/{runid}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/aysrun/"+runid
        return self.client.get(uri, headers=headers, params=query_params)


    def executeRun(self, data, runid, repository, headers=None, query_params=None):
        """
        execute an aysrun
        It is method for POST /ays/repository/{repository}/aysrun/{runid}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/aysrun/"+runid
        return self.client.post(uri, data, headers=headers, params=query_params)


    def createBlueprint(self, data, repository, headers=None, query_params=None):
        """
        Create a new blueprint
        It is method for POST /ays/repository/{repository}/blueprint
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/blueprint"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def listBlueprints(self, repository, headers=None, query_params=None):
        """
        List all blueprint
        It is method for GET /ays/repository/{repository}/blueprint
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/blueprint"
        return self.client.get(uri, headers=headers, params=query_params)


    def deleteBlueprint(self, blueprint, repository, headers=None, query_params=None):
        """
        delete blueprint
        It is method for DELETE /ays/repository/{repository}/blueprint/{blueprint}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/blueprint/"+blueprint
        return self.client.session.delete(uri, headers=headers, params=query_params)


    def getBlueprint(self, blueprint, repository, headers=None, query_params=None):
        """
        Get a blueprint
        It is method for GET /ays/repository/{repository}/blueprint/{blueprint}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/blueprint/"+blueprint
        return self.client.get(uri, headers=headers, params=query_params)


    def executeBlueprint(self, data, blueprint, repository, headers=None, query_params=None):
        """
        Execute the blueprint
        It is method for POST /ays/repository/{repository}/blueprint/{blueprint}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/blueprint/"+blueprint
        return self.client.post(uri, data, headers=headers, params=query_params)


    def updateBlueprint(self, data, blueprint, repository, headers=None, query_params=None):
        """
        Update existing blueprint
        It is method for PUT /ays/repository/{repository}/blueprint/{blueprint}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/blueprint/"+blueprint
        return self.client.put(uri, data, headers=headers, params=query_params)


    def archiveBlueprint(self, data, blueprint, repository, headers=None, query_params=None):
        """
        archive the blueprint
        It is method for PUT /ays/repository/{repository}/blueprint/{blueprint}/archive
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/blueprint/"+blueprint+"/archive"
        return self.client.put(uri, data, headers=headers, params=query_params)


    def restoreBlueprint(self, data, blueprint, repository, headers=None, query_params=None):
        """
        restore the blueprint
        It is method for PUT /ays/repository/{repository}/blueprint/{blueprint}/restore
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/blueprint/"+blueprint+"/restore"
        return self.client.put(uri, data, headers=headers, params=query_params)


    def destroyRepository(self, data, repository, headers=None, query_params=None):
        """
        destroy repo without deleting it from FS
        It is method for POST /ays/repository/{repository}/destroy
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/destroy"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def listServices(self, repository, headers=None, query_params=None):
        """
        List all services in the repository
        It is method for GET /ays/repository/{repository}/service
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/service"
        return self.client.get(uri, headers=headers, params=query_params)


    def listServicesByRole(self, role, repository, headers=None, query_params=None):
        """
        List all services of role 'role' in the repository
        It is method for GET /ays/repository/{repository}/service/{role}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/service/"+role
        return self.client.get(uri, headers=headers, params=query_params)


    def getServiceByName(self, name, role, repository, headers=None, query_params=None):
        """
        Get a service by its name
        It is method for GET /ays/repository/{repository}/service/{role}/{name}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/service/"+role+"/"+name
        return self.client.get(uri, headers=headers, params=query_params)


    def deleteServiceByName(self, name, role, repository, headers=None, query_params=None):
        """
        delete a service and all its children
        It is method for DELETE /ays/repository/{repository}/service/{role}/{name}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/service/"+role+"/"+name
        return self.client.session.delete(uri, headers=headers, params=query_params)


    def listTemplates(self, repository, headers=None, query_params=None):
        """
        list all templates
        It is method for GET /ays/repository/{repository}/template
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/template"
        return self.client.get(uri, headers=headers, params=query_params)


    def getTemplate(self, name, repository, headers=None, query_params=None):
        """
        Get a template
        It is method for GET /ays/repository/{repository}/template/{name}
        """
        uri = self.client.base_url + "/ays/repository/"+repository+"/template/"+name
        return self.client.get(uri, headers=headers, params=query_params)


    def addTemplateRepo(self, data, headers=None, query_params=None):
        """
        add a new actor template repository
        It is method for POST /ays/template_repo
        """
        uri = self.client.base_url + "/ays/template_repo"
        return self.client.post(uri, data, headers=headers, params=query_params)


    def listAYSTemplates(self, headers=None, query_params=None):
        """
        list all AYS templates
        It is method for GET /ays/templates
        """
        uri = self.client.base_url + "/ays/templates"
        return self.client.get(uri, headers=headers, params=query_params)


    def getAYSTemplate(self, name, headers=None, query_params=None):
        """
        get an AYS template
        It is method for GET /ays/templates/{name}
        """
        uri = self.client.base_url + "/ays/templates/"+name
        return self.client.get(uri, headers=headers, params=query_params)
