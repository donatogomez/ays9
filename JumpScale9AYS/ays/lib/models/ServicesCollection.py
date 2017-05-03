from js9 import j
from JumpScale9AYS.ays.lib.models.ServiceModel import ServiceModel
from JumpScale9Lib.data.capnp.ModelBase import ModelBaseCollection
import capnp
from JumpScale9AYS.ays.lib import model_capnp as ModelCapnp


class ServicesCollection(ModelBaseCollection):
    """
    This class represent a collection of AYS Services contained in an AYS repository
    It's used to list/find/create new Instance of Service Model object
    """

    def __init__(self, repository):
        self.repository = repository
        namespace = "ays:%s:service" % repository.name
        db = j.data.kvs.getMemoryStore(namespace, namespace)
        self.services = {}
        self.logger = j.logger.get('j.core.atyourservice.service-collection')

        super().__init__(
            schema=ModelCapnp.Service,
            category="Service",
            namespace=namespace,
            modelBaseClass=ServiceModel,
            db=db,
            indexDb=db
        )

    def new(self):
        model = ServiceModel(
            aysrepo=self.repository,
            key='',
            new=True,
            collection=self)
        return model

    def get(self, key):
        model = ServiceModel(
            aysrepo=self.repository,
            key=key,
            new=False,
            collection=self)
        return model

    def list(self, name="", actor="", state="", parent="", producer="", returnIndex=False):
        """
        @param name can be the full name e.g. myappserver or a prefix but then use e.g. myapp.*
        @param actor can be the full name e.g. node.ssh or role e.g. node.* (but then need to use the .* extension, which will match roles)
        @param parent is in form $actorName!$instance
        @param producer is in form $actorName!$instance

        @param state:
            new
            installing
            ok
            error
            disabled
            changed

        """
        if name == "":
            name = ".*"
        if actor == "":
            actor = ".*"
        if state == "":
            state = ".*"

        if parent == "":
            parent = ".*"
        elif parent.find("!") == -1:
            raise j.exceptions.Input(message="parent needs to be in format: $actorName!$instance",
                                     level=1, source="", tags="", msgpub="")
        if producer == "":
            producer = ".*"
        elif producer.find("!") == -1:
            raise j.exceptions.Input(message="producer needs to be in format: $actorName!$instance",
                                     level=1, source="", tags="", msgpub="")
        regex = "%s:%s:%s:%s:%s" % (name, actor, state, parent, producer)
        return self._index.list(regex, returnIndex=returnIndex)

    def find(self, name="", actor="", state="", parent="", producer=""):
        """
        @param name can be the full name e.g. myappserver or a prefix but then use e.g. myapp.*
        @param actor can be the full name e.g. node.ssh or role e.g. node.* (but then need to use the .* extension, which will match roles)
        @param parent is in form $actorName!$instance
        @param producer is in form $actorName!$instance

        @param state:
            new
            installing
            ok
            error
            disabled
            changed

        """
        res = []
        for key in self.list(name, actor, state, producer=producer, parent=parent):
            res.append(self.get(key))
        return res
