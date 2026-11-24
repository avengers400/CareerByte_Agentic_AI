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

## Concepts to notice

- `if`/`elif` branches are evaluated in order; the first matching branch is selected.
- Lists can be changed after creation, while tuples are intended to remain fixed.
- Sets remove duplicates but do not guarantee a predictable display order.
- A dictionary maps keys to values; the list example demonstrates several ways to inspect dictionary content.
