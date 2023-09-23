#!/usr/bin/python3
"""
Script runs flask web application.
listens on 0.0.0.0, port 5000.
"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Returns rendered html with data from db
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
