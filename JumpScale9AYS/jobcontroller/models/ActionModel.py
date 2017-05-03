from js9 import j
from JumpScale9Lib.data.capnp.ModelBase import ModelBase


class ActionModel(ModelBase):
    """
    object which has info required to execute a method (an action)
    """

    @property
    def imports(self):
        return ""

    @property
    def code(self):
        return self.dbobj.code

    @code.setter
    def code(self, val):
        val = val.rstrip() + "\n"
        if "ipshell" in val:
            self.dbobj.debug = True
        elif "from pudb" in val:
            self.dbobj.debug = True
        else:
            self.dbobj.debug = False
        self.dbobj.code = val

    @property
    def argsText(self):
        if self.dbobj.args == "":
            return ""
        return self.dbobj.args
        #     return {}
        # return msgpack.loads(self.dbobj.args, encoding='utf-8')

    # @property
    # def argsJons(self):
    #     ddict2 = OrderedDict(self.args)
    #     return j.data.serializer.json.dumps(ddict2, sort_keys=True, indent=True)

    @argsText.setter
    def argsText(self, val):
        # args = msgpack.dumps(val)
        if j.data.types.string.check(val) is False:
            raise j.exceptions.Input(message="args input need to be string", level=1, source="", tags="", msgpub="")
        val = val.rstrip(":) ")
        val = val.rstrip(":) ")
        self.dbobj.args = val

    @property
    def key(self):
        if self._key == "":
            self._key = j.data.hash.md5_string(self.dbobj.name + self.dbobj.code + self.argsText)
        return self._key

    def index(self):
        # put indexes in db as specified
        ind = "%s:%s" % (self.dbobj.origin, self.dbobj.name)
        self.collection._index.index({ind: self.key})

    def _post_init(self):
        self.dbobj.logStdout = True
        self.dbobj.log = True
        self.dbobj.remember = True

    def _pre_save(self):
        pass

    # @property
    # def dictFiltered(self):
    #     ddict = self.dbobj.to_dict()
    #     # if "args" in ddict:
    #     #     ddict.pop("args")
    #     return ddict

    def __repr__(self):
        out = self.dictJson + "\n"
        # if self.dbobj.args not in ["", b""]:
        #     out += "args:\n"
        #     out += self.argsJons
        return out

    __str__ = __repr__
