#!/usr/bin/python3
# FileStorage class serializes instances to JSON files
# and deserializes JSON files files to instances

import json
from os import path


class FileStorage:
    '''Defines a FileStorage class for serialization to JSON
        and deserialization to instances

    Attributes:
        __file_path: String. Path to JSON file
        __objects: Dict. Stores objects with key <class name>.id
    '''
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        '''Instantiates a class object
        '''
        pass

    def all(self):
        '''Returns the dictionary __objects
        '''
        return type(self).__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to store in __objects
        '''
        key = type(obj).__name__ + '.' + obj.id
        type(self).__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file
        '''
        json.dump(type(self).__objects, type(self).__file_path)

    def reload(self):
        '''Deserializes the JSON file to __objects if the file exists;
            Otherwise do nothing (raise no exception)
        '''
        if path.exists(type(self).__file_path):
            type(self).__objects = json.load(type(self).__file_path)
