import json
import os

from dotenv import load_dotenv

from flask import Flask


load_dotenv()

app = Flask(__name__)


@app.route('/data/<username>')
def handle_main_route(username):
    pass


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
