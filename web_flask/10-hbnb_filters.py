#!/usr/bin/python3
""" Flask Routing Template """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.state import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_states_list():
    """ retrieve list of states and passes to template"""
    # states_list = storage.all(State)
    states_list = []
    list_amenities = []
    dic_states = storage.all(State)
    dic_amenities = storage.all(Amenity)
    for state in dic_states.values():
        states_list.append(state)
    for amenity in dic_amenities.values():
        list_amenities.append(amenity)
    return render_template('10-hbnb_filters.html', states=states_list, amenities=list_amenities)


@app.teardown_appcontext
def teardown_db(exception):
    '''close connections'''
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # app.run()
