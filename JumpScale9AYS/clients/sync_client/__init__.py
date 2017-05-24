import requests


from .AYSRun import AYSRun
from .AYSRunListing import AYSRunListing
from .AYSStep import AYSStep
from .Action import Action
from .ActionRecurring import ActionRecurring
from .Actor import Actor
from .Blueprint import Blueprint
from .BlueprintListing import BlueprintListing
from .CreateBlueprintReqBody import CreateBlueprintReqBody
from .CreateRepositoryReqBody import CreateRepositoryReqBody
from .EnumAYSRunListingState import EnumAYSRunListingState
from .EnumActionState import EnumActionState
from .EnumSchedulerStatus import EnumSchedulerStatus
from .Error import Error
from .Event import Event
from .Job import Job
from .Log import Log
from .NameListing import NameListing
from .Repository import Repository
from .Scheduler import Scheduler
from .Service import Service
from .ServiceData import ServiceData
from .ServicePointer import ServicePointer
from .Template import Template
from .TemplateConfig import TemplateConfig
from .TemplateLink import TemplateLink
from .TemplateListing import TemplateListing
from .TemplateRecurringAction import TemplateRecurringAction
from .TemplateRepo import TemplateRepo
from .UpdateBlueprintReqBody import UpdateBlueprintReqBody

from .client import Client as APIClient

from .oauth2_client_itsyouonline import Oauth2ClientItsyouonline

class Client:
    def __init__(self, base_uri="https://localhost:5000"):
        self.api = APIClient(base_uri)
        self.oauth2_client_itsyouonline = Oauth2ClientItsyouonline()