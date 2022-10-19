import json

from abc import ABC
from request.request_template import RequestTemplate


class GappleRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://api.gapple.pw/status/' + data['uuid'])
        parsed_data = json.loads(await response.text())

        data['account_type'] = parsed_data['status']
