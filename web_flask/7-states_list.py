#!/usr/bin/python3

'''Is all about getting'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

app.config['strict_slashes'] = False


@app.teardown_appcontext
def errorhandles(self):
    from models import storage
    storage.close()


@app.route('/states_list')
def index():
    items = storage.all(State)
    return render_template('7-states_list.html', items=items)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
