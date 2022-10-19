from abc import ABC
from request.request_template import RequestTemplate


class MineplexRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://www.mineplex.com/players/' + username)
        data['has_played_mineplex'] = response.status == 200

