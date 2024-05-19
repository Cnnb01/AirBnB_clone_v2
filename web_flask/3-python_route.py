#!/usr/bin/python3
"""
This script defines a simple Flask
web application that responds with
"Hello, HBNB!" to incoming requests.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    A view function that returns a simple response.
    """
    return "Hello, HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    A view function that returns a simple HBNB response.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    A view function that returns a simple HBNB response.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text):
    """
    A view function that returns a simple HBNB response.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
