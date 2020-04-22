#!/usr/bin/python3
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
    ''' display “Hello HBNB!" '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ define route /hbnb and return a text"""
    return 'HBNB'


@app.route('/c/<text>',  strict_slashes=False)
def c(text):
    # show the text after slash
    return 'C %s' % escape(text.replace("_", " "))

if __name__ == "__main__":
    app.run()
