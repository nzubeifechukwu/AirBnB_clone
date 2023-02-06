# AirBnB Clone
In this project, we will build a simple clone of the [AirBnB website](https://www.airbnb.com/).

The project will be done in parts across four months, each part reflecting the students' level of knowledge at that point in the ALX SE programme.

For this, the very first part of the project, our focus is on building the console (or command line interpreter).

## The Command Line Interpreter
Like a shell, the command line will help us manipulate data without a visual interface. Using our command line interpreter, we want to be able to do the following:
* Create a new object
* Retrieve an object from a file, a database, etc.
* Do operations on objects, e.g. count, compute stats, etc.
* Update attributes of an object
* Destroy an object
### Execution
The interpreter should work in interactive mode:
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
It should also work in non-interactive mode:
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
All tests should also pass in non-interactive mode: ```$ echo "python3 -m unittest discover tests" | bash```
