import json

from abc import ABC
from request.request_template import RequestTemplate


class WynncraftRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://api.wynncraft.com/v2/player/' + username + '/stats')

        if response.status != 200:
            data['has_played_wynncraft'] = False
            return

        data['has_played_wynncraft'] = True

        parsed_data = json.loads(await response.text())

        data['wynncraft_first_join'] = parsed_data['firstJoin']
        data['wynncraft_last_join'] = parsed_data['lastJoin']
