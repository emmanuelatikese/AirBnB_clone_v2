#!/usr/bin/python3
'''this is about the webframework'''

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index(text='is cool'):
    text = text.replace('_', ' ')
    return ('Python %s' % text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
