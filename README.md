# The AirBnB Clone Project

## Project Overview
This project is the initial phase of the AirBnB clone project, focusing on developing the backend and integrating it with a console application using the cmd module in Python.

Data generated by the application, in the form of Python objects, is stored in a JSON file and can be accessed using the JSON module in Python.

## Command Interpreter Description
The command-line interface of the application resembles the Bash shell but with a limited set of accepted commands tailored for the AirBnB website usage.

The command interpreter serves as the frontend of the web app, allowing users to interact with the backend developed using Python's object-oriented programming (OOP) paradigm.

Available commands include:
- show
- create
- update
- destroy
- count

These commands facilitate various operations on objects, including creation, retrieval, updating, and deletion.

## Getting Started
These instructions will help you set up the project on your local Linux machine for development and testing purposes.

### Installation

Clone the project repository from GitHub, which includes the console program and its dependencies.


After cloning the repository, you'll find a folder named AirBnB_clone containing the necessary files for the program.

- `console.py`: Main executable of the project, the command interpreter.
- `models/engine/file_storage.py`: Class for serializing instances to a JSON file and deserializing JSON files to instances.
- `models/__init__.py`: Initialization file with a unique `FileStorage` instance for the application.
- `models/base_model.py`: Class defining common attributes/methods for other classes.
- `models/user.py`: User class inheriting from BaseModel.
- `models/state.py`: State class inheriting from BaseModel.
- `models/city.py`: City class inheriting from BaseModel.
- `models/amenity.py`: Amenity class inheriting from BaseModel.
- `models/place.py`: Place class inheriting from BaseModel.
- `models/review.py`: Review class inheriting from BaseModel.

## Usage
The program can operate in two modes: Interactive and Non-interactive.

### Interactive Mode
In interactive mode, the console displays a prompt (hbnb), allowing users to enter commands and execute them.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-interactive Mode
In non-interactive mode, commands are piped into the shell's execution for immediate processing without displaying a prompt.

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


### Command Input Format
Commands must be provided with proper arguments and options, separated by spaces.

Example:

```

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

```

or

```
user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
```


## Available Commands
The command interpreter recognizes the following commands and their respective functionalities:

|Command| Description |
|--|--|
| **quit or EOF** | Exit the program |
| **help** | Display help text for a command |
| **create** | Create a new instance of a valid class |
| **show** | Print the string representation of an instance |
| **destroy** | Delete an instance |
| **all** | Print all instances of a class |
| **update** | Update attributes of an instance |
| **count** | Retrieve the number of instances of a class |

## Author

Abdulahi Abass

