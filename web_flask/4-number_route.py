#!/usr/bin/python
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: display “C ” followed by the value of the text
    /python/<text>: display “Python ”
    followed by the value of the text
    /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Displays 'Python' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
