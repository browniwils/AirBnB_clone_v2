#!/usr/bin/python3
"""
Script starts a Flask web application.
listens on 0.0.0.0, default port 5000.
"""
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns Hello HBNB!
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns HBNB!
    """
    return "HBNB!"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Returns 'C' concantenated with arg <text>
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Returns Python concantenated with arg <text>
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)