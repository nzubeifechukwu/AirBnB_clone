#!/usr/bin/python3
# FileStorage class serializes instances to JSON files
# and deserializes JSON files files to instances

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''Defines a FileStorage class for serialization to JSON
        and deserialization to instances

    Attributes:
        __file_path: String. Path to JSON file
        __objects: Dict. Stores objects with key <class name>.id
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        '''Returns all objects of type cls in __objects
        '''
        obj_dict = {}
        for key, value in self.__objects.items():
            if type(value) == cls:
                obj_dict[key] = value
        return obj_dict

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to store in __objects
        '''
        key = type(obj).__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file
        '''
        dict_obj = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dict_obj, f)

    def reload(self):
        '''Deserializes the JSON file to __objects if the file exists;
            Otherwise do nothing (raise no exception)
        '''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                objs = json.load(f)
                for k, v in objs.items():
                    if k not in self.__objects:
                        name = v['__class__']
                        # create a new object of type name
                        obj = eval(f'{name}(**v)')
                        self.new(obj)
        except Exception:
            pass

    def delete(self, obj=None):
        '''Deletes obj from __objects
        '''
        if obj is None:
            pass
        else:
            for key, value in self.__objects.items():
                if value == obj:
                    obj_key = key
                    break
            del self.__objects[obj_key]
