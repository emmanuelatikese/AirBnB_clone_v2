#!/usr/bin/python3
"""This is all about markupsafe"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

app.config['strict_slashes=False'] = False


@app.route('/c/<text>')
def rite_txt(text):
    text = text.replace("_", " ")
    return ('C %s' % escape(text))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
