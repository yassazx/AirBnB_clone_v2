#!/usr/bin/python3

"""
This script that starts a Flask web application
info:
    web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNBi”
    /c/<text>: display “C ” followed by the value of the
    text variable (replace underscore _ symbols with a space )
    uses the option strict_slashes=False in your route definition
    /python/(<text>): display “Python ”, followed by the
    value of the text variable (replace underscore _ symbols
    with a space )
The default value of text is “is cool”
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Returns:
            A string
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns:
            A string
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """
    Returns:
         “C ” followed by the value of the text
         variable (replace underscore _ symbols with a space
    """
    if "_" in text:
        new_str = text.replace('_', ' ')
        return "C {}".format(new_str)
    else:
        return "C {}".format(text)


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Returns:
            Python ”, followed by the value of the text
            variable (replace underscore _ symbols with a space )
    """
    if "_" in text:
        new_str = text.replace('_', ' ')
        return "Python {}".format(new_str)
    else:
        return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
