#!/usr/bin/python3
""" Command interpreter console """

import cmd
import sys
from models.base_model import BaseModel

CLASSES = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    ''' Entry point of the command interpreter '''
    prompt = "(hbnb) "

    def emptyline(self):
        """ Ignore empty spaces """
        pass

    def do_quit(self, arg):
        ''' Quit command to exit the program '''
        return True

    def do_EOF(self, arg):
        ''' Exit the program '''
        return True

    def do_create(self, arg):
        '''Creates a new instance of BaseModel'''
        if len(arg) < 1:
            print("** class name missing **")
            return False

        split_arg = arg.split()
        if split_arg[0] in CLASSES:
            new = CLASSES[split_arg[0]]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        '''Prints the string representation of an instance'''

        split_arg = arg.split()
        if len(split_arg) < 1:
            print("** class name missing **")
            return False

        if split_arg[0] not in CLASSES:
            print("** class doesn't exist **")
            return False

        if len(split_arg) == 1:
            print("** instance id missing **")
            return False

        storage = FileStorage()
        storage.reload()
        data_storage = storage.all()
        key = "{}.{}".format(split_arg[0], split_arg[1])
        if key not in data_storage.keys():
            print("** no instance found **")
            return False
        print(data_storage[key])

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        split_arg = split.split()
        if len(split_arg) == 0:
            print("** class name missing **")
            return False

        if len(split_arg) == 1:
            print("** instance id missing **")
            return False

        if split_arg[0] not in CLASSES:
            print("** class doesn't exist **")

        storage = FileStorage()
        storage.reload()
        data_storage = storage.all()
        key = "{}.{}".format(split_arg[0], split_arg[1])

        if key not in data_storage.keys():
            print("** no instance found **")
            return False

        del data_storage[key]
        storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all
        instances based or not on the class name.'''

        split_arg = split.split()
        storage = FileStorage()
        storage.reload()
        data_storage = storage.all()
        all_data = []

        if not len(split_arg):
            for obj in data_storage.values():
                all_data.append(obj.__str__())
        else:
            if split_arg[0] not in CLASSES:
                print("** class doesn't exist **")
                return False
            for obj in data_storage.values():
                if split_arg[0] == obj.__class__.__name__:
                    all_data.append(obj.__str__())
        print(all_data)

    def do_update(self, arg):
            """Update specific attribute of a class instance of
            a given <id>
            Usage:
            update <class name> <id> <attribute name> "<attribute value>"
            """
            arg_split = arg.split()

            if not len(arg_split):
                print("** class name missing **")
                return False

            if arg_split[0] not in CLASSES:
                print("** class doesn't exist **")
                return False

            if len(arg_split) == 1:
                print("** instance id missing **")
                return False

            if len(arg_split) == 2:
                print("** attribute name missing **")
                return False

            if len(arg_split) == 3:
                print("** value missing **")
                return False

            else:
                storage = FileStorage()
                data_storage = storage.all()
                key = "{}.{}".format(arg_split[0], arg_split[1])
                if key in data_storage.keys():
                    setattr(data_storage[key], arg_split[2], arg_split[3])
                    storage.save()
                else:
                    print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()