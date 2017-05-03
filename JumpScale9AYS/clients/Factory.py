from JumpScale9AYS.clients.sync_client import Client


class Factory:

    def __init__(self):
        self.__jslocation__ = "j.clients.atyourservice"

    def get(self, base_uri="http://localhost:5000"):
        return Client(base_uri=base_uri)
