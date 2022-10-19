import json

from abc import ABC
from request.request_template import RequestTemplate


class UsernameHistoryRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://laby.net/api/v2/user/' + data['uuid'] + '/get-profile')
        parsed_data = json.loads(await response.text())

        username_history = parsed_data['username_history']
        names = []
        for name in username_history:
            names.append({
                'name': name,
                'changed_at': name['changed_at']
            })

        data['names'] = names
