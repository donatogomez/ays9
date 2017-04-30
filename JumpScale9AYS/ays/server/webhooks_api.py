import json as JSON

import asyncio
from sanic.response import json, text
import jsonschema
from jsonschema import Draft4Validator
from js9 import j

import os
dir_path = os.path.dirname(os.path.realpath(__file__))


async def webhooks_github_post(request):
    '''
    Endpoint that receives the events from github
    It is handler for POST /webhooks/github
    '''
    if request.headers.get('Content-Type') != 'application/json':
        return json({'error': 'wront content type'}, 400)

    event = request.headers.get('X-GitHub-Event')
    payload = request.json
    for repo in j.core.atyourservice.aysRepos.list():
        for service in repo.services:
            await service.processEvent(
                channel='webservice',
                command=event,
                secret=None,
                tags={},
                payload=payload
            )

    return json({"event executed"}, 200)


async def webhooks_events_post(request):
    '''
    Endpoint that receives generic events
    It is handler for POST /webhooks/events
    '''
    if request.headers.get('Content-Type') != 'application/json':
        return json({'error': 'wront content type'}, 400)

    # in the case of a webhooks event we pass the original request object in the payload
    payload = request.json.get('payload', {})
    payload['request'] = request

    coros = []
    for repo in j.core.atyourservice.aysRepos.list():
        for service in repo.services:
            coros.append(service.processEvent(
                channel='webservice',
                command=request.json.get('command'),
                secret=request.json.get('secret'),
                tags=request.json.get('tags'),
                payload=payload,
            ))

    try:
        result = await asyncio.gather(*coros)
        return json({}, 200)
    except Exception as err:
        return json({'errror': str(err)}, 500)
