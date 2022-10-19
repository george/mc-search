import json

from abc import ABC
from request.request_template import RequestTemplate


class CapesMeRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://capes.me/api/user/' + username)

        if response.status == 404:
            return {}

        parsed_data = json.loads(await response.text())
        capes = []

        for cape in parsed_data['capes']:
            if not bool(cape['removed']):
                capes.append(cape['type'])
        data['capes'] = capes
