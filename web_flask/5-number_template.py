#!/usr/bin/python3
"""
This script defines a simple Flask
web application that responds with
"Hello, HBNB!" to incoming requests.
"""

from flask import Flask, render_template

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


@app.route("/c/<string:text>", strict_slashes=False)
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


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_a_number(n):
    """
    A view function that returns a simple HBNB response.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_is_a_number_template(n):
    """
    A view function that returns a simple HBNB response.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
