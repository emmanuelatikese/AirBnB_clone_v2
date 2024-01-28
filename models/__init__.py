#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage

type_storage = getenv('HBNB_TYPE_STORAGE')

storage = FileStorage() if type_storage == 'fs' else DBStorage()
storage.reload()
