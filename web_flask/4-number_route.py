#!/usr/bin/python3
'''This is about the number'''

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.config['strict_slashes'] = False


@app.route('/number/<int:n>')
def index(n):
    return ('%d is a number' % n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
