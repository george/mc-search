import os
import json
import asyncio
import requests

from flask import Flask
from dotenv import load_dotenv
from aiohttp import ClientSession

from request.impl.gapple_request import GappleRequest
from request.impl.capes_me_request import CapesMeRequest

load_dotenv()

app = Flask(__name__)
web_requests = [
    CapesMeRequest(),
    GappleRequest()
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

    # print(data)
    return data


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
