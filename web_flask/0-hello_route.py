#!/usr/bin/python3
# A script to start a web app on port 5000 and return Hello HBNB!
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
   return "<p> Hello HBNB! </p>"
