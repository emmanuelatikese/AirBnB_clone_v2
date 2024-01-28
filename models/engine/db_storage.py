#!/usr/bin/python3

"""Is all about the db"""

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.place import place_amenity

lists = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}

class DBStorage:
    '''As said earlier'''

    __engine, __session = None, None

    def __init__(self):
        """This start to initialize"""
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           HBNB_MYSQL_USER,
                                           HBNB_MYSQL_PWD,
                                           HBNB_MYSQL_HOST,
                                           HBNB_MYSQL_DB
                                       ), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            """We listing everything"""
            new_dict = {}
            if cls is None:
                for cl in lists.values():
                    ob = self.__session.query(cl).all()
                    for x in ob:
                        k = key = x.__class__.__name__ + '.' + x.id
                        new_dict[k] = x
            else:
                ob = self.__session.query(cls).all()
                for x in ob:
                    key = x.__class__.__name__ + '.' + x.id
                    new_dict[key] = x
            return new_dict

        def new (self, obj):
            if obj:
                try:
                    self.__session.add(obj)
                    self.__session.flush()
                    self.__session.refresh()
                except Exception as err:
                    self.__session.rollback()
                    raise err

        def save(self):
            '''This is here to save'''
            self.__session.commit()
        
        def delete(self, obj=None):
            if obj:
                self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

        def reload(self):
            '''This is here to reload'''
            Base.metadata.create_all(self.__engine)
            sess_fact = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
            self.__session = scoped_session(sess_fact)()

        def close():
            self.__session.close()
