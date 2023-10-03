#!/usr/bin/python3
"""
Script starts a Flask web application.
listens on 0.0.0.0, default port 5000.
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

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

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Returns `n` is a number only if n is an integer
    """
    if isinstance(n, int):
        return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number_template(n):
    """
    Return rendered html template if `n` is integer
    """
    if isinstance(n, int):
        return render_template("5-number.html", num=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Return rendered html template if `n` is integer
    """
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
