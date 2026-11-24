# Object-Oriented Programming

These lessons introduce object-oriented programming (OOP) through server and student classes. They progress from defining a class and creating instances to inheritance and different method decorators.

## Examples

| File | What it demonstrates |
|---|---|
| [1-first_class.py](1-first_class.py) | Declaring a class, creating an object, reading a class attribute, and calling an instance method. |
| [2-init-constructor.py](2-init-constructor.py) | Initializing each `Server` instance with its own name and CPU value. |
| [3-modify-object-attributes.py](3-modify-object-attributes.py) | Updating an instance attribute through an instance method. |
| [4-inheritance.py](4-inheritance.py) | Extending a base `Server` class, calling the parent initializer with `super()`, and reusing a health-check method. |
| [5-Method-overriding.py](5-Method-overriding.py) | Replacing an inherited method implementation in a subclass. |
| [6-static-method.py](6-static-method.py) | Defining a static validation helper that does not need instance state. |
| [7-class-method.py](7-class-method.py) | Using a class method to access a class-level attribute. |
| [introduction.txt](introduction.txt) | Informal notes on server attributes, methods, and the motivation for classes. |

## Run

Run each Python file individually from this directory, for example:

```powershell
python .\1-first_class.py
```

The examples use only Python's standard language features and require no extra packages.

## Concepts to notice

- A class describes shared structure and behavior; an object is an instance of that class.
- `self` refers to the instance whose method is being called.
- Instance attributes belong to an individual object; class attributes are shared through the class.
- Inheritance allows a subclass to reuse and extend a base class.
- An overridden method provides subclass-specific behavior with the same method name.
- `@staticmethod` does not receive an implicit instance or class argument; `@classmethod` receives the class as `cls`.
