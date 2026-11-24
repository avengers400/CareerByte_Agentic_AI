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

## Concepts to notice

- Parameters are names a function receives; `return` sends a result back to its caller.
- `*args` gathers extra positional arguments, while `**kwargs` gathers extra named arguments.
- A lambda is a concise expression for a small function; use a named function when the logic needs more explanation.
- JSON is a text representation for data exchange. `json.dumps()` produces JSON text, and `json.loads()` parses JSON text.
- The docstring example is intentionally simple; its annotation and conditional illustrate syntax rather than comprehensive input validation.
