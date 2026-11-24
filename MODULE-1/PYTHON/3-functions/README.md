# Functions and JSON

The scripts in this folder show how to organize behavior into functions, pass flexible arguments, and use functions as values. The last lesson introduces JSON conversion with Python's standard-library `json` module.

## Examples

| File | What it demonstrates |
|---|---|
| [1-func-basics.py](1-func-basics.py) | Defining and calling functions, parameters, return values, and a CPU-status helper. |
| [2-args-kwargs.py](2-args-kwargs.py) | Variable-length positional arguments (`*args`) and keyword arguments (`**kwargs`). |
| [3-lambda-function.py](3-lambda-function.py) | Lambda expressions and using a lambda as a sorting key for server records. |
| [4-higher-order-function.py](4-higher-order-function.py) | Passing a function into another function and calling it there. |
| [5-docstring.py](5-docstring.py) | A function with a return annotation and a docstring-style description. |
| [6-understanding_json.py](6-understanding_json.py) | Converting Python dictionaries to JSON text and parsing JSON text into Python values. |

## Run

From this directory, run an example such as:

```powershell
python .\1-func-basics.py
```

Each file is independent and uses only Python's standard library.

## Concepts explained

### Defining and calling functions

A function is a named, reusable block of code. A `def` statement defines it; calling its name runs its body. **Parameters** are the names in the definition, and **arguments** are the values supplied when calling it. A function can use `return` to send a result to its caller. If it only prints a value, that output is displayed but is not automatically returned for later calculations.

### Flexible arguments

The `*servers` syntax collects any extra positional arguments into a tuple. The `**servers` syntax collects named arguments into a dictionary. These patterns are useful when the number or names of inputs may vary; the examples iterate over the collected values.

### Lambda and higher-order functions

A lambda is a small anonymous function written as an expression, for example `lambda x: x**2`. It is often useful as a short callback or sort key. A **higher-order function** accepts another function as an argument or returns a function. The monitor example accepts a check function and applies it to a value, separating the operation from the specific rule.

### Docstrings and annotations

A **docstring** is a string placed at the start of a function (or other definition) to describe its purpose; documentation tools can expose it. A **type annotation** such as `-> float` communicates an intended input or output type to readers and tools. Python does not automatically enforce that annotation at runtime. The current docstring example places its documentation string inside a conditional rather than at the start of the function, so it does not serve as the function's official docstring.

### JSON

JSON is a text format for exchanging structured data. Python dictionaries and lists can represent JSON objects and arrays. `json.dumps()` converts a Python value to JSON text; `json.loads()` parses JSON text back into Python values. For file objects, the corresponding functions are `json.dump()` and `json.load()`, shown in the [file reading and writing guide](../file-reading-writing/README.md).
