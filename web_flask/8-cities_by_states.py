#!/usr/bin/python3
""" A script to run a flask web application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_bystate():
    """ Displays an html page with alist of all states and related cities"""
    states = storage.all("State")
    return render_template("8-cities_by_states.py", states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Remove the current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
