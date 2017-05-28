from js9 import j
from JumpScale9Lib.data.capnp.ModelBase import ModelBaseCollection
import capnp
from JumpScale9AYS.ays.lib import model_capnp as ModelCapnp
from JumpScale9AYS.ays.lib.models.ActorModel import ActorModel


class ActorsCollection(ModelBaseCollection):
    """
    This class represent a collection of AYS Actors contained in an AYS repository
    It's used to list/find/create new Instance of Actor Model object
    """

    def __init__(self, repository):
        self.repository = repository
        namespace = "ays:%s:actor" % repository.name
        db = j.data.kvs.getMemoryStore(namespace, namespace)
        self.logger = j.logger.get('j.atyourservice.server.actor-collection')
        # cache for the actors objects
        self.actors = {}
        super().__init__(
            schema=ModelCapnp.Actor,
            category="Actor",
            namespace=namespace,
            modelBaseClass=ActorModel,
            db=db,
            indexDb=db
        )

    def new(self):
        model = ActorModel(
            aysrepo=self.repository,
            key='',
            new=True,
            collection=self)
        return model

    def get(self, key):
        model = ActorModel(
            aysrepo=self.repository,
            key=key,
            new=False,
            collection=self)
        return model

    def _list_keys(self, name="", state="", returnIndex=False):
        """
        @param name can be the full name e.g. node.ssh or a rule but then use e.g. node.*  (are regexes, so need to use .* at end)
        @param state
            new
            ok
            error
            disabled
        """
        if name == "":
            name = ".*"
        if state == "":
            state = ".*"
        regex = "%s:%s" % (name, state)
        return self._index.list(regex, returnIndex=returnIndex)

    def find(self, name="", state=""):
        """
        @param name can be the full name e.g. node.ssh or a rule but then use e.g. node.*  (are regexes, so need to use .* at end)
        @param state
            new
            ok
            error
            disabled
        """
        res = []
        for key in self._list_keys(name, state):
            res.append(self.get(key))
        return res

    def destroy(self):
        super().destroy()
        self.actors = {}
        self.logger = None
