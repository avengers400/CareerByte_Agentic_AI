# Python Fundamentals

This folder contains the Python lessons for Module 1. Its scripts use simple server, CPU, and memory examples to make language concepts concrete. Each `.py` file is a separate exercise and should be run on its own with Python 3.

## Recommended sequence

1. [1-datatypes](1-datatypes/README.md) — values, variables, types, operators, conversions, input, and a server-usage report.
2. [2-statements-loops-list-dict-set-tuple.py](2-statements-loops-list-dict-set-tuple.py/README.md) — conditions and collection types. The directory name ends in `.py`, but it is a folder.
3. [3-functions](3-functions/README.md) — reusable functions and JSON serialization.
4. [error-handling](error-handling/README.md) — handling expected exceptions and cleanup.
5. [file-reading-writing](file-reading-writing/README.md) — reading and writing text and JSON files.
6. [oops](oops/README.md) — object-oriented programming concepts.

## Concepts covered

The course begins with Python's basic building blocks and gradually combines them into larger ideas:

- **Variables and types** give names to values and describe whether information is text (`str`), a whole number (`int`), a decimal (`float`), or a Boolean (`bool`).
- **Operators and expressions** calculate results or compare values. Converting input to a numeric type is necessary before doing numeric calculations.
- **Conditions and iteration** control which statements run and how often; lists and other collections provide values to process.
- **Functions** make behavior reusable. Arguments pass information into a function, and return values pass results back.
- **Exceptions and file operations** support handling runtime problems and exchanging information with files. JSON provides a text format for structured data.
- **Object-oriented programming** models entities as objects that combine attributes (data) with methods (behavior), with inheritance and method overriding as reuse mechanisms.

## Requirements and running scripts

- Install Python 3 and make the `python` command available in a terminal.
- Run a script by passing its path to Python, for example:

  ```powershell
  python .\1-datatypes\1-first-file.py
  ```

- Run interactive scripts in a terminal so you can respond to their prompts.
- Run one example at a time. These lessons do not share program state.

No third-party packages are needed for the examples as currently written. One collection example imports `requests` but does not use it; that import can still require the package to be installed in the selected Python environment.

## File-path note

The file I/O scripts include absolute paths rooted in the original author's `C:\Users\HP\Downloads\Agentic-Ai` checkout. Those paths will not work on most other machines or checkout locations. Update them to point to the local sample files, or use paths relative to the script, before running those examples; details are in the [file I/O guide](file-reading-writing/README.md).
