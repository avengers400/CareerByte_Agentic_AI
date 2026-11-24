# Conditions, Loops, and Collections

Despite its `.py` suffix, this path is a **directory** containing Python lessons. The examples introduce decision-making and common built-in collection types using CPU checks, server names, and sample records.

## Examples

| File | What it demonstrates |
|---|---|
| [1-if-else.py](1-if-else.py) | `if`/`else` branching based on an integer CPU input and a threshold. |
| [2-if-else-elif.py](2-if-else-elif.py) | A three-way status decision using `if`, `elif`, and `else`. |
| [3-and-or-condition.py](3-and-or-condition.py) | Combining conditions with boolean `and` and `or`. |
| [4-list.py](4-list.py) | List indexing, length, mutation, slicing, iteration, `continue`, and introductory dictionary examples. |
| [5-tuple.py](5-tuple.py) | Ordered, immutable tuples, iteration, slicing, and tuple unpacking. |
| [7-set.py](7-set.py) | Unique values in sets, adding/removing items, and converting a list to sorted unique values. |

There is no `6-*.py` lesson in this folder; the existing numbering is preserved.

## Run

Run one file at a time from this directory. For example:

```powershell
python .\1-if-else.py
```

The first example asks for CPU usage. The other examples use values defined in their source files and print results directly.

## Concepts explained

### Conditions and Boolean logic

An `if` statement runs a block only when its condition is true. `else` gives an alternative path, while `elif` adds another condition to test. Python checks branches from top to bottom and executes only the first matching branch. Comparisons such as `cpu >= 90` evaluate to `True` or `False`. The Boolean operators `and` and `or` combine conditions: `and` requires both conditions to be true; `or` requires at least one.

### Lists and iteration

A **list** is an ordered, changeable collection. Its elements can be accessed by index, including negative indices from the end. Lists support adding and removing elements, slicing a portion, and iteration with `for`. In a loop, `continue` skips the remainder of the current iteration and proceeds to the next item. The list lesson also introduces dictionaries and shows accessing values by key.

### Tuples

A **tuple** is an ordered collection that cannot be changed after it is created. It is useful for a fixed group of related values. Tuples support indexing, slicing, iteration, and **unpacking**, which assigns tuple elements to multiple variables in one statement.

### Sets

A **set** contains unique elements and does not provide positional indexing. Adding an element already present does not create a duplicate. Sets are useful when uniqueness matters, such as removing repeated values from a list. Their iteration and printed order should not be relied on.

### Dictionaries

A **dictionary** stores key-value pairs. Keys provide named access to their corresponding values, which is often clearer than relying on numeric positions. The example uses indexing, `.get()`, `.items()`, `.keys()`, and `.values()` to retrieve or inspect dictionary data.
