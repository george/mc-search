import json

from abc import ABC
from request.request_template import RequestTemplate


class LabyModRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://laby.net/api/user/' + data['uuid'] + '/get-game-stats')
        parsed_data = json.loads(await response.text())

        if parsed_data['first_joined']:
            data['labymod_first_join'] = parsed_data['first_joined']
        if parsed_data['last_online']:
            data['labymod_last_online'] = parsed_data['last_online']
