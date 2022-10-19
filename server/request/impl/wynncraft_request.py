import json

from abc import ABC
from request.request_template import RequestTemplate


class WynncraftRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://api.wynncraft.com/v2/player/' + username + '/stats')

        parsed_data = json.loads(await response.text())

        data['has_played_wynncraft'] = 'firstJoin' in parsed_data

        if 'firstJoin' in parsed_data:
            data['wynncraft_first_join'] = parsed_data['firstJoin']
        if 'lastJoin' in parsed_data:
            data['wynncraft_last_join'] = parsed_data['lastJoin']
