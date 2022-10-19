import os
import json

from abc import ABC
from datetime import datetime
from request.request_template import RequestTemplate


class HypixelApiRequest(RequestTemplate, ABC):

    async def complete(self, session, username, data):
        response = await session.get('https://api.hypixel.net/player?key=' + os.getenv('HYPIXEL_API_KEY') + '&uuid=' + data['uuid'])
        parsed_data = json.loads(await response.text())

        if parsed_data['player']:
            player_data = parsed_data['player']

            firstLogin = int(player_data['firstLogin']) / 1000
            data['first_hypixel_join'] = datetime.fromtimestamp(firstLogin).strftime('%m-%d-%Y')

            if player_data['lastLogin']:
                lastLogin = int(player_data['lastLogin']) / 1000
                data['last_hypixel_join'] = datetime.fromtimestamp(lastLogin).strftime('%m-%d-%Y')
