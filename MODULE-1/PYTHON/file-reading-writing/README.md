# Reading and Writing Text and JSON Files

This folder demonstrates basic file operations with Python's `open()` context manager and the standard-library `json` module. The text files and JSON documents provide sample input and output for the scripts.

## Files

| File | Purpose |
|---|---|
| [read-json.py](read-json.py) | Reads `server.json` as JSON and prints its `LogicalID` entry; also reads and prints `sample.txt`. |
| [write-json.py](write-json.py) | Serializes a Python dictionary into formatted JSON in `server1.json`. |
| [write-text.py](write-text.py) | Writes several lines to `write-sample.txt`. |
| [server.json](server.json) | Example nested JSON document used by the reader. |
| [server1.json](server1.json) | JSON output target and example document for the writer. |
| [sample.txt](sample.txt) | Text input read by `read-json.py`. |
| [write-sample.txt](write-sample.txt) | Text output content represented in the folder; running the writer replaces this file's contents. |

## Important path setup

The scripts currently use absolute paths that point to the original author's Windows checkout (`C:\Users\HP\Downloads\Agentic-Ai\...`). Update those paths to match your local checkout before running `read-json.py`, `write-json.py`, or `write-text.py`. Alternatively, use paths relative to the script or current working directory.

Run each script from this directory after confirming its paths:

```powershell
python .\read-json.py
python .\write-json.py
python .\write-text.py
```

The writer examples modify `server1.json` and `write-sample.txt` respectively. Review their contents before and after execution.

## Concepts to notice

- `with open(..., encoding="utf-8")` closes a file automatically when the block ends.
- `json.load()` reads and parses JSON directly from an open file; `json.dump()` writes a Python value as JSON.
- `json.dump(..., indent=4)` formats the output for readability.
- Opening a file with mode `"w"` replaces existing file contents. Use that mode carefully when practicing.
