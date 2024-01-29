#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage

ts = getenv('HBNB_TYPE_STORAGE')

if ts == 'fs':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
