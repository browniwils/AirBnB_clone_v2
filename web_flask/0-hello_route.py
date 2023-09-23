#!/usr/bin/python3
"""
Script starts a Flask web application.
listens on 0.0.0.0, default port 5000.
with home Route /: displays 'Hello HBNB!'
"""
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns Hello HBNB!
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
