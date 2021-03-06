#!/usr/bin/python3
""" Flask Routing Template """
from flask import Flask
from markupsafe import escape
from flask import render_template
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
    '''show the text after slash'''
    # show the text after slash
    return 'Python %s' % escape(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' show integer'''
    # show the text after slash
    return '%d is a number' % n


@app.route('/number_template/')
@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/')
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run()
