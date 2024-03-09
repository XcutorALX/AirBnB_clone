#!/usr/bin/python3
import re
import cmd
import models
import shlex
import json
"""The entry point of the ciommand interpreter"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classMapping = {
                "BaseModel": models.base_model.BaseModel,
                "User": models.user.User,
                "State": models.state.State,
                "City": models.city.City,
                "Amenity": models.amenity.Amenity,
                "Place": models.place.Place,
                "Review": models.review.Review
            }

    @staticmethod
    def emptyline():
        pass

    @staticmethod
    def precmd(line):
        """Executes before line is interpreted"""

        r = "(\w+\.\w+)\((.*)\)"
        m = re.search(r, line)
        if not m:
            return line
        else:
            args = m.group(1).split('.')
            param = m.group(2).replace("{", "'{").replace("}", "}'")
            param = param.split(',')
            param = [ i.strip(" ") for i in param ]
            line = " ".join(param)
            return (f'{args[1]} {args[0]} {line}')

    def do_count(self, arg):
        """Counts the instances of a class"""

        args = shlex.split(arg)
        length = len(args)
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classMapping:
            print("** class doesn't exist **")
        else:
            cls = HBNBCommand.classMapping[args[0]]
            objs = models.storage.all()
            num = sum([type(objs[i]) == cls for i in objs])
            print(num)

    def do_update(self, arg):
        """ Updates an instance based on the class name and\
                id by adding or updating attribute"""

        args = shlex.split(arg)
        length = len(args)
        objs = models.storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classMapping:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objs:
            print("** no instance found **")
        elif length < 3:
            print("** attribute name missing **")
        else:
            print(args[2])
            param = shlex.split(args[2])
            pattern = r'"(\w+)": "?(\w+)"?'
            key = f"{args[0]}.{args[1]}"
            matches = re.findall(pattern, args[2])
            if matches:
                for m in matches:
                    print(m)
                    setattr(objs[key], m[0], m[1])
            elif length < 4:
                    print("** value missing **")
            else:
                setattr(objs[key], args[2], args[3])
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances\
            based or not on the class name."""
        if not arg:
            for val in models.storage.all().values():
                print(val)
        else:
            args = arg.split(" ")
            if args[0] in HBNBCommand.classMapping:
                for val in models.storage.all().values():
                    if type(val) == HBNBCommand.classMapping[args[0]]:
                        print(val)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        args = shlex.split(arg)
        length = len(args)

        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classMapping:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in objs:
                del objs[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_create(self, arg):
        """Creates an instance of the specified class i.e (create <class>)"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classMapping:
            print("** class doesn't exist **")
        else:
            inst = HBNBCommand.classMapping[arg]()
            inst.save()
            print(inst.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the\
class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        args = shlex.split(arg)
        length = len(args)

        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classMapping:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return (True)

    def do_EOF(self, arg):
        """EOF character to exit the program"""
        print()
        return (True)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
