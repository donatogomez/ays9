from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import text
from JumpScale9AYS.ays.server import webhooks_api


webhooks_if = Blueprint('webhooks_if')


class webhooks_eventsView(HTTPMethodView):
    
    async def post(self, request):
     
        return await webhooks_api.webhooks_events_post(request)
    
webhooks_if.add_route(webhooks_eventsView.as_view(), '/webhooks/events')

class webhooks_githubView(HTTPMethodView):
    
    async def post(self, request):
     
        return await webhooks_api.webhooks_github_post(request)
    
webhooks_if.add_route(webhooks_githubView.as_view(), '/webhooks/github')

