#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import make_response

import json
import os

from werkzeug.exceptions import NotFound



application = Flask(__name__)
dirname = os.path.dirname(__file__)
with open(os.path.join(dirname, "users.json"), "r") as f:
    users = json.load(f)
    print(users)


@application.route("/", methods=['GET'])
def index():
    return pretty_json({
        "resources": {
            "users": "/users",
            "user": "/users/<username>",
        },
        "current_uri": "/"
    })


@application.route("/users", methods=['GET'])
def all_users():
    return pretty_json(users)


@application.route("/users/<username>", methods=['GET'])
def user_data(username):
    if username not in users:
        raise NotFound

    return pretty_json(users[username])


@application.route("/users/<username>/something", methods=['GET'])
def user_something(username):
    raise NotImplementedError()


def pretty_json(arg):
    response = make_response(json.dumps(arg, sort_keys=True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response


def create_test_app():
    app = Flask(__name__)
    return app


if __name__ == "__main__":
    application.run(port=5000)
