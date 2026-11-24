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

## Concepts explained

### Classes, objects, and attributes

A **class** defines a type by grouping data and operations that belong together. An **object** (or instance) is a concrete value created from that class. In the server examples, a server object can hold attributes such as its name and CPU usage and provide methods such as a health check. Attributes are values associated with an object or class.

### Initializers and `self`

`__init__` is the initializer Python calls after creating a new instance. It commonly assigns instance-specific values, such as `self.name = name`. The parameter `self` refers to the particular instance receiving the method call, which lets the method read or update that instance's attributes. It is supplied automatically when an instance method is called.

### Instance attributes and class attributes

An **instance attribute** belongs to one object, so different instances can hold different values. A **class attribute** is defined on the class and is shared unless an instance overrides it with an attribute of the same name. The student example's `school` value is a class attribute.

### Inheritance and overriding

Inheritance defines a subclass based on an existing class. The subclass can reuse parent behavior, add its own attributes and methods, or customize behavior. `super()` lets the subclass call the parent's implementation; the EC2 server example uses it to initialize the inherited name and CPU attributes. **Method overriding** occurs when a subclass defines a method with the same name as one inherited from its parent; calls on subclass instances use the subclass implementation.

### Instance, static, and class methods

- An **instance method** receives `self` and can use or modify data belonging to that object.
- A **static method**, marked with `@staticmethod`, receives neither `self` nor `cls` automatically. It is placed in a class because it is related conceptually, not because it needs class or instance state.
- A **class method**, marked with `@classmethod`, receives the class as `cls`. It can read or update class-level data and works with subclasses through the class used to call it.

These method forms help communicate what state an operation needs. They do not make attributes private; Python uses naming conventions rather than enforced access modifiers for most ordinary attributes.
