#!/usr/bin/env python3
"""command line interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """definition of class"""
    prompt = "(hbnb) "

    def do_create(self, line):
        if len(line) <= 0:
            print("** class name missing **")
        else:
            try:
                my_Obj = BaseModel()
            except NameError:
                print("** class doesn't exist **")

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
