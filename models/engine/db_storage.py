#!/usr/bin/python3
'''DBStorage class defines a MySQL database storage engine
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    '''Defines the DBStorage class
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''Instantiates a DBStorage class
        '''
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}', pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Query all objects on the current database session,
            depending on the class name. If cls is None, query all object types

        Return: a dictionary of all objects,
            with key = <class-name>.<object-id> and value = object
        '''
        obj_dict = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = type(obj).__name__ + '.' + obj.id
                obj_dict[key] = obj
        else:
            for cls_name in (User, State, City, Amenity, Place, Review):
                for obj in self.__session.query(cls_name).all():
                    key = type(obj).__name__ + '.' + obj.id
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        '''Add object to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''Commit all changes in the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''Delete object from the current database session if it is None
        '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''Create all the table in the database
            Then create a database session from the engine
        '''
        Base.metadata.create_all(self.__engine)
        sess_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_fac)
        self.__session = Session()
