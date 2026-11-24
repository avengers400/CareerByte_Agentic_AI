# Data Types, Variables, and Input

This folder starts the Python course with values and simple expressions, then applies them to server monitoring examples. Read the numbered scripts in order.

## Examples

| File | What it demonstrates |
|---|---|
| [1-first-file.py](1-first-file.py) | Running a Python file and printing text with `print()`. |
| [2-variables-and-datatypes.py](2-variables-and-datatypes.py) | Assigning values to variables and inspecting string, integer, and boolean types with `type()`. |
| [3-operator-and-typeconversion.py](3-operator-and-typeconversion.py) | Comparisons, numeric conversion, string methods, membership checks, and formatted strings. |
| [4-user-input.py](4-user-input.py) | Collecting text from the terminal with `input()` and including it in output. |
| [5-mini-project.py](5-mini-project.py) | Reading server name, CPU, and memory usage; reporting whether values exceed fixed thresholds. |

## Run

From this directory, execute an individual example with:

```powershell
python .\1-first-file.py
```

The input examples pause for responses in the terminal. In the mini project, CPU and memory are converted to floating-point numbers; enter numeric values such as `72` or `72.5`.

## Concepts explained

### Values, variables, and types

A **value** is a piece of data used by a program. A **variable** is a name that refers to a value, such as `server_name = "newgen-server"`. Python associates every value with a type. The examples include strings (`str`) for names and text, integers (`int`) for whole-number counts, floating-point numbers (`float`) for measurements with decimals, and Booleans (`bool`) for `True` or `False` states. `type(value)` reveals the value's current type.

### Operators and conversion

Operators perform work on values. Arithmetic operators calculate, while comparison operators such as `>`, `==`, and `!=` produce Boolean results. A number written inside quotes is still text: `"60" + 10` is not valid numeric addition. Convert it first with `int("60")` or `float("60.5")`, depending on whether a fractional value is possible.

### Text operations and formatted strings

String methods such as `.lower()` and `.upper()` return text in a changed case. The `in` operator checks whether a substring occurs inside another string. An f-string, written like `f"Server {name}"`, inserts the current value of an expression into text and is useful for constructing readable reports.

### Terminal input and the mini project

`input()` displays a prompt and returns the user's response as a string. Convert numeric responses before comparing them to numeric thresholds. The mini project reads server name, CPU, and memory, then uses comparisons to report whether CPU is over 80% or memory is over 85%. These are simple threshold checks, not full validation: for example, the script does not reject negative usage or a value above 100%.
