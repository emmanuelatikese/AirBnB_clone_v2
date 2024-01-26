#!/usr/bin/python3
'''This is all about hbbh'''

from flask import Flask

web = Flask(__name__)

@web.route('/hbnb', strict_slashes=False)
def index():
    return ('HBNB')

if __name__ == "__main__":
    web.run(host='0.0.0.0', port=5000)
