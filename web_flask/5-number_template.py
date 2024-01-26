#!/usr/bin/python3
'''This is about render'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/number_template/<int:n>", strict_slashes=False)
def index(n=None):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
