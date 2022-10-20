import json

from abc import ABC
from request.request_template import RequestTemplate


class NameMCRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://api.namemc.com/profile/' + data['uuid'] + '/friends')

        if response.status != 200:
            return

        parsed_data = json.loads(await response.text())

        data['namemc_friends'] = parsed_data
