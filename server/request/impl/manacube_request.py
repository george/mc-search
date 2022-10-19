import json

from abc import ABC
from request.request_template import RequestTemplate


class ManacubeRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://manacube.com/stats_data/fetch.php?uuid=' + data['uuid'])
        parsed_data = json.loads(await response.text())

        exists = parsed_data['exists']

        data['has_played_manacube'] = exists

        if exists:
            data['manacube_level'] = parsed_data['level']
            data['manacube_rank'] = parsed_data['rank']
