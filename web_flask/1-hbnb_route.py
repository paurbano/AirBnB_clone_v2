#!/usr/bin/python3
""" Route flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/',  strict_slashes=False)
def index():
    ''' display “Hello HBNB!" '''
    return 'Hello HBNB!'


@app.route('/hbnb',  strict_slashes=False)
def hbnb():
    """ define route /hbnb and return a text"""
    return 'HBNB'

if __name__ == "__main__":
    app.run()
