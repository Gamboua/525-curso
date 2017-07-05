#!/usr/bin/python

from flask import Flask
from uuid import uuid4

from blueprints.ListContainers import ListContainers
from blueprints.RemoveContainers import RemoveContainers

app = Flask(__name__)
app.secret_key = str(uuid4())

app.register_blueprint(ListContainers)
app.register_blueprint(RemoveContainers)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)