from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import text
from JumpScale9AYS.ays.server import ays_api
from JumpScale9AYS.ays.server.oauth2_itsyouonline import oauth2_itsyouonline

ays_if = Blueprint('ays_if')


async def auth(request, func):
    code, msg = await oauth2_itsyouonline(["user:memberof:organization"]).check_token(request)
    if code != 200:
        return text(msg, code)
    return await func

class ays_reloadView(HTTPMethodView):

    async def post(self, request):
        return await auth(request, ays_api.reload(request))

ays_if.add_route(ays_reloadView.as_view(), '/ays/reload')

class ays_repositoryView(HTTPMethodView):

    async def get(self, request):
        return await auth(request, ays_api.listRepositories(request))

    async def post(self, request):
        return await auth(request, ays_api.createRepository(request))

ays_if.add_route(ays_repositoryView.as_view(), '/ays/repository')

class ays_repository_byrepositoryView(HTTPMethodView):

    async def get(self, request, repository):
        return await auth(request, ays_api.getRepository(request, repository))

    async def delete(self, request, repository):
        return await auth(request, ays_api.deleteRepository(request, repository))

ays_if.add_route(ays_repository_byrepositoryView.as_view(), '/ays/repository/<repository>')

class ays_repository_byrepository_actorView(HTTPMethodView):

    async def get(self, request, repository):
        return await auth(request, ays_api.listActors(request, repository))

ays_if.add_route(ays_repository_byrepository_actorView.as_view(), '/ays/repository/<repository>/actor')

class ays_repository_byrepository_actor_byactorView(HTTPMethodView):

    async def get(self, request, actor, repository):
        return await auth(request, ays_api.getActorByName(request, actor, repository))

    async def put(self, request, actor, repository):
        return await auth(request, ays_api.updateActor(request, actor, repository))

ays_if.add_route(ays_repository_byrepository_actor_byactorView.as_view(), '/ays/repository/<repository>/actor/<actor>')

class ays_repository_byrepository_aysrunView(HTTPMethodView):

    async def get(self, request, repository):
        return await auth(request, ays_api.listRuns(request, repository))

    async def post(self, request, repository):
        return await auth(request, ays_api.createRun(request, repository))

ays_if.add_route(ays_repository_byrepository_aysrunView.as_view(), '/ays/repository/<repository>/aysrun')

class ays_repository_byrepository_aysrun_byrunidView(HTTPMethodView):

    async def get(self, request, runid, repository):
        return await auth(request, ays_api.getRun(request, runid, repository))

    async def post(self, request, runid, repository):
        return await auth(request, ays_api.executeRun(request, runid, repository))

    async def delete(self, request, runid, repository):
       return await auth(request, ays_api.deleteRun(request, runid, repository))

ays_if.add_route(ays_repository_byrepository_aysrun_byrunidView.as_view(), '/ays/repository/<repository>/aysrun/<runid>')

class ays_repository_byrepository_blueprintView(HTTPMethodView):

    async def get(self, request, repository):
        return await auth(request, ays_api.listBlueprints(request, repository))

    async def post(self, request, repository):
        return await auth(request, ays_api.createBlueprint(request, repository))

ays_if.add_route(ays_repository_byrepository_blueprintView.as_view(), '/ays/repository/<repository>/blueprint')

class ays_repository_byrepository_blueprint_byblueprintView(HTTPMethodView):

    async def get(self, request, blueprint, repository):
        return await auth(request, ays_api.getBlueprint(request, blueprint, repository))

    async def post(self, request, blueprint, repository):
        return await auth(request, ays_api.executeBlueprint(request, blueprint, repository))

    async def put(self, request, blueprint, repository):
        return await auth(request, ays_api.updateBlueprint(request, blueprint, repository))

    async def delete(self, request, blueprint, repository):
        return await auth(request, ays_api.deleteBlueprint(request, blueprint, repository))

ays_if.add_route(ays_repository_byrepository_blueprint_byblueprintView.as_view(), '/ays/repository/<repository>/blueprint/<blueprint>')

class ays_repository_byrepository_blueprint_byblueprint_archiveView(HTTPMethodView):

    async def put(self, request, blueprint, repository):
        return await auth(request, ays_api.archiveBlueprint(request, blueprint, repository))

ays_if.add_route(ays_repository_byrepository_blueprint_byblueprint_archiveView.as_view(), '/ays/repository/<repository>/blueprint/<blueprint>/archive')

class ays_repository_byrepository_blueprint_byblueprint_restoreView(HTTPMethodView):

    async def put(self, request, blueprint, repository):
        return await auth(request, ays_api.restoreBlueprint(request, blueprint, repository))

ays_if.add_route(ays_repository_byrepository_blueprint_byblueprint_restoreView.as_view(), '/ays/repository/<repository>/blueprint/<blueprint>/restore')

class ays_repository_byrepository_destroyView(HTTPMethodView):

    async def post(self, request, repository):
        return await auth(request, ays_api.destroyRepository(request, repository))

ays_if.add_route(ays_repository_byrepository_destroyView.as_view(), '/ays/repository/<repository>/destroy')

class ays_repository_byrepository_serviceView(HTTPMethodView):

    async def get(self, request, repository):
        return await auth(request, ays_api.listServices(request, repository))

ays_if.add_route(ays_repository_byrepository_serviceView.as_view(), '/ays/repository/<repository>/service')

class ays_repository_byrepository_service_byroleView(HTTPMethodView):

    async def get(self, request, role, repository):
        return await auth(request, ays_api.listServicesByRole(request, role, repository))

ays_if.add_route(ays_repository_byrepository_service_byroleView.as_view(), '/ays/repository/<repository>/service/<role>')

class ays_repository_byrepository_service_byrole_bynameView(HTTPMethodView):

    async def get(self, request, name, role, repository):
        return await auth(request, ays_api.getServiceByName(request, name, role, repository))

    async def delete(self, request, name, role, repository):
        return await auth(request, ays_api.deleteServiceByName(request, name, role, repository))

ays_if.add_route(ays_repository_byrepository_service_byrole_bynameView.as_view(), '/ays/repository/<repository>/service/<role>/<name>')

class ays_repository_byrepository_templateView(HTTPMethodView):

    async def get(self, request, repository):
        return await auth(request, ays_api.listTemplates(request, repository))

ays_if.add_route(ays_repository_byrepository_templateView.as_view(), '/ays/repository/<repository>/template')

class ays_repository_byrepository_template_bynameView(HTTPMethodView):

    async def get(self, request, name, repository):
        return await auth(request, ays_api.getTemplate(request, name, repository))

ays_if.add_route(ays_repository_byrepository_template_bynameView.as_view(), '/ays/repository/<repository>/template/<name>')

class ays_template_repoView(HTTPMethodView):

    async def post(self, request):
        return await auth(request, ays_api.addTemplateRepo(request))

ays_if.add_route(ays_template_repoView.as_view(), '/ays/template_repo')

class ays_templatesView(HTTPMethodView):

    async def get(self, request):
        return await auth(request, ays_api.listAYSTemplates(request))

ays_if.add_route(ays_templatesView.as_view(), '/ays/templates')

class ays_templates_bynameView(HTTPMethodView):

    async def get(self, request, name):
        return await auth(request, ays_api.getAYSTemplate(request, name))

ays_if.add_route(ays_templates_bynameView.as_view(), '/ays/templates/<name>')

class ays_repository_byrepository_schedulerView(HTTPMethodView):

    async def get(self, request, repository):

        if not await oauth2_itsyouonline(["user:memberof:organization"]).check_token(request):
            return text('', 401)

        return await ays_api.getSchedulerStatus(request, repository)

ays_if.add_route(ays_repository_byrepository_schedulerView.as_view(), '/ays/repository/<repository>/scheduler')


class ays_repository_byrepository_scheduler_runs_runningView(HTTPMethodView):

    async def get(self, request, repository):

        if not await oauth2_itsyouonline(["user:memberof:organization"]).check_token(request):
            return text('', 401)

        return await ays_api.getCurrentRun(request, repository)

ays_if.add_route(ays_repository_byrepository_scheduler_runs_runningView.as_view(), '/ays/repository/<repository>/scheduler/running')
