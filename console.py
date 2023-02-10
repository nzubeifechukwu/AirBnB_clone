#!/usr/bin/env python3
"""command line interpreter"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """definition of class"""
    prompt = "(hbnb) "
    __classes = ['BaseModel']

    def do_create(self, line):
        if len(line) <= 0:
            print("** class name missing **")
            return
        arguments = line.split()
        if arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        my_object = eval(arguments[0])()
        if my_object:
            my_object.save()
            print(my_object.id)

    def do_show(self, line):
        """prints the string representation of an instance
        based on id and class name
        """
        if len(line) <= 0:
            print("** class name missing **")
            return
        arguments = line.split()
        if arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arguments) < 2:
            print("** instance id missing **")
            return
        my_obj_dict = models.storage.all()
        if "{}.{}".format(arguments[0], arguments[1]) not in my_obj_dict:
            print("** no instance found **")
            return
        print(my_obj_dict["{}.{}".format(arguments[0], arguments[1])])

    def do_destroy(self, line):
        """deletes an instance based on a class name and id. Save"""
        if len(line) <= 0:
            print("** class name missing **")
            return
        arguments = line.split()
        if arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist** ")
            return
        if len(arguments) < 2:
            print("** instance id missing **")
            return
        my_obj_dict = models.storage.all()
        if "{}.{}".format(arguments[0], arguments[1]) not in my_obj_dict:
            print("** no instance found** ")
            return
        my_obj_dict.pop("{}.{}".format(arguments[0], arguments[1]))
        models.storage.save()

    def do_all(self, line):
        """prints all string representation of all instances
        based or not on class name"""
        arguments = line.split()
        my_obj_dict = models.storage.all()
        res = []
        if len(line) > 0:
            if arguments[0] in HBNBCommand.__classes:
                for v in my_obj_dict.values():
                    res.append(str(v))
            else:
                print("** class doesn't exist **")
                return
        else:
            for val in my_obj_dict.values():
                res.append(str(val))
        print(res)

    def do_update(self, line):
        """updates an instance based on the class name and id. save"""
        my_obj_dict = models.storage.all()
        if len(line) <= 0:
            print("** class name missing **")
            return
        arguments = line.split()
        if arguments[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arguments) < 2:
            print("** instance id missing **")
            return
        if "{}.{}".format(arguments[0], arguments[1]) not in my_obj_dict:
            print("** no instance found ** ")
            return
        if len(arguments) < 3:
            print("** attribute name missing **")
            return
        if len(arguments) < 4:
            print("** value missing **")
            return
        if len(arguments) > 4:
            del arguments[4:]
        if arguments[3].startswith('"'):
            arguments[3] = arguments[3].replace('"', '')
        setattr(my_obj_dict["{}.{}".format(arguments[0],
                arguments[1])], arguments[2], arguments[3])
        models.storage.save()

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """do nothing for an empty line + Enter"""
        pass

    def do_EOF(self, line):
        """exit shell when end of file (ctrl+D)"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()