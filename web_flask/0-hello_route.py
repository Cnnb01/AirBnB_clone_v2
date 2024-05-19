#!/usr/bin/python3
"""
This script defines a simple Flask
web application that responds with
"Hello, HBNB!" to incoming requests.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    A view function that returns a simple HTML response.
    """
    return "<p>Hello, HBNB!</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
