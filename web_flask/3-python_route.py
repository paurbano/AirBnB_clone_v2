#!/usr/bin/python3
""" Flask Routing """
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
    ''' display “Hello HBNB!" '''
    return 'Hello HBNB!'


@app.route('/hbnb',  strict_slashes=False)
def hbnb():
    """ define route /hbnb and return a text"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    ''' show the text after slash '''
    # show the text after slash
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text=""):
    '''Use defaults values'''
    # show the text after slash
    return 'Python %s' % escape(text.replace("_", " "))

if __name__ == "__main__":
    app.run()
