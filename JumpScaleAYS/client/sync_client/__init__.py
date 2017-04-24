import requests

from .client import Client as APIClient

from .oauth2_client_itsyouonline import Oauth2ClientItsyouonline

class Client:
    def __init__(self, base_uri="http://localhost:5000"):
        self.api = APIClient(base_uri)

        self.oauth2_client_itsyouonline = Oauth2ClientItsyouonline()
