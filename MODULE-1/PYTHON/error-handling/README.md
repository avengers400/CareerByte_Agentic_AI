# Error Handling

This folder contains short examples of handling exceptions so a program can respond to common failures instead of terminating without an explanation.

## Examples

| File | What it demonstrates |
|---|---|
| [try-except-block.py](try-except-block.py) | Catching `ZeroDivisionError` and continuing execution afterward. |
| [try-except-finally-block.py](try-except-finally-block.py) | Catching conversion and division errors, then running a `finally` block. |
| [example-1.py](example-1.py) | Handling a missing file separately from other exceptions. |

## Run

From this directory, run an example with:

```powershell
python .\try-except-block.py
```

The `try-except-finally-block.py` example asks for a number. Try a valid non-zero integer, `0`, or non-numeric text to observe different outcomes.

## File example note

`example-1.py` tries to open `sample.txt` using a path relative to the **current working directory**. There is no `sample.txt` in this folder; a sample text file exists in [file-reading-writing](../file-reading-writing/README.md). Consequently, running this example from this folder currently exercises its missing-file handling unless you provide the expected file in the working directory or adjust the path.

## Concepts explained

### Exceptions and `try`/`except`

An **exception** represents an event that interrupts the normal flow of a program, such as dividing by zero, converting invalid text to a number, or opening a missing file. Put statements that might fail in a `try` block. An `except` block handles a matching exception, allowing the program to give a useful message or take another action. Catching a specific exception, such as `ValueError` or `FileNotFoundError`, makes the response more precise.

### Multiple error cases

A `try` block can have several `except` clauses. Python checks them in order and runs the first one that matches the raised exception. The input example demonstrates that invalid numeric text (`ValueError`) and division by zero (`ZeroDivisionError`) are distinct problems and can be handled separately.

### The `finally` block

A `finally` block runs whether the `try` block completed successfully or raised an exception. It is intended for cleanup or actions that must happen on either path. In the example, it prints a completion message regardless of the input result.

### Error handling boundaries

An exception that is not caught by a matching handler continues propagating up the call stack and may terminate the program. Avoid catching every possible exception without a clear reason: broad handlers can conceal programming mistakes. The examples are introductory; in production code, catch expected exception types and report enough context to diagnose the problem.
