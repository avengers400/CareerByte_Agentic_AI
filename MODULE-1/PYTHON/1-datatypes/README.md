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

## Concepts to notice

- `input()` returns text. Convert it explicitly when arithmetic or numeric comparison is needed.
- A value's type affects the operations available to it; for example, `"75.5"` is a string until converted.
- The mini project compares input with thresholds of 80% CPU and 85% memory. It reports whether each limit was exceeded; it does not validate that values are within the 0–100 range.
