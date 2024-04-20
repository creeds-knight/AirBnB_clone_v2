#!/usr/bin/python3
"""A script to start a web app on port 5000 and return Hello HBNB!"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ displays variable"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """displays python followed by value of text"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/python', strict_slashes=False)
def python():
    """ returns python is cool"""
    return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def prnt_number(n):
    """ returns n """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def disp_number(n):
    """ return a web page if the number is an int"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
