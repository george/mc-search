import os
import asyncio
import platform
import requests

from flask import Flask
from dotenv import load_dotenv
from aiohttp import ClientSession

from request.impl.gapple_request import GappleRequest
from request.impl.mineplex_request import MineplexRequest
from request.impl.namemc_request import NameMCRequest
from request.impl.capes_me_request import CapesMeRequest
from request.impl.laby_mod_request import LabyModRequest
from request.impl.manacube_request import ManacubeRequest
from request.impl.wynncraft_request import WynncraftRequest
from request.impl.hypixel_api_request import HypixelApiRequest
from request.impl.username_history_request import UsernameHistoryRequest

load_dotenv()

app = Flask(__name__)
web_requests = [
    NameMCRequest(),
    GappleRequest(),
    CapesMeRequest(),
    LabyModRequest(),
    MineplexRequest(),
    ManacubeRequest(),
    WynncraftRequest(),
    HypixelApiRequest(),
    UsernameHistoryRequest()
]


async def complete(request, session, username, data):
    await request.complete(session, username, data)


async def complete_requests(username, data):
    async with ClientSession() as session:
        tasks = []
        for request in web_requests:
            tasks.append(complete(request, session, username, data))
        await asyncio.gather(*tasks)


@app.route('/data/<username>')
def handle_main_route(username):
    data = {}

    ashcon_data = requests.get('https://api.ashcon.app/mojang/v2/user/' + username).json()

    data['username'] = ashcon_data['username']
    data['uuid'] = ashcon_data['uuid']

    asyncio.run(complete_requests(username, data))

    return data


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
