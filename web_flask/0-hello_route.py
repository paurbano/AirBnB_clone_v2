#!/usr/bin/python3
''' Routing Flask '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    ''' display “Hello HBNB!" '''
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run()
