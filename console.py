#!/usr/bin/python3
import cmd
import models
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

    def do_update(self, arg):
        """ Updates an instance based on the class name and\
                id by adding or updating attribute"""

        args = arg.split(" ")
        length = len(args)
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classMapping:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in models.storage.all():
            print("** no instance found **")
        elif length < 3:
            print("** attribute name missing **")
        elif length < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            setattr(models.storage.all()[key], args[2], args[3])
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

        args = arg.split(" ")
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
        args = arg.split(" ")
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
