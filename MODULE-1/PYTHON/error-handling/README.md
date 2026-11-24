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

The examples are for learning. In production code, prefer catching the specific exceptions you expect and provide useful context when reporting failures.
