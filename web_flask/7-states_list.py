#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db():
    """
    closes the database connection
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state():
    """
    displays states in asc order
    """
    state = storage.all(State)
    return render_template("7-states_list.html", state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
