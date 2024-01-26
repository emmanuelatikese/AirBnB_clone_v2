#!/usr/bin/python3
'''This is odd or even'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def index(n=None):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
