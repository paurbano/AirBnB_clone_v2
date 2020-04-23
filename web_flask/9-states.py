#!/usr/bin/python3
""" Flask Routing Template """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.state import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states_list(id=None):
    """ retrieve list of states and passes to template"""
    # states_list = storage.all("State")
    states_list = []
    dic_states = storage.all(State)
    for state in dic_states.values():
        # for city in dic_cities.values():
        if id is not None and state.id == id:
            return render_template('9-states.html', state=state, id=id)
        else:
            states_list.append(state)

    return render_template('9-states.html', states=states_list, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    '''close connections'''
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
