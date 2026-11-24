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

## Concepts explained

### Opening and closing files

`open(path, mode, encoding="utf-8")` creates a file object for reading or writing. The `with` statement is a context manager: it closes the file automatically when its indented block ends, even if an error occurs. A relative path is interpreted from the process's current working directory; an absolute path specifies a location from the filesystem root.

### Reading and writing text

The `"r"` mode opens an existing file for reading. Calling `.read()` returns its contents as a string. The `"w"` mode opens a file for writing and replaces existing contents (or creates the file if it does not exist). Calling `.write(text)` writes a string; newline characters such as `\n` separate lines.

### JSON and Python values

JSON represents structured values as text, using objects, arrays, strings, numbers, Booleans, and `null`. Python's `json` module translates between JSON and corresponding Python values. `json.load(file)` parses JSON from an open file; `json.dump(value, file)` serializes a value to an open file. `indent` controls whitespace for readability, not the underlying data.

### Side effects and paths

Reading depends on the path resolving to an existing file and, for JSON, valid JSON content. Writing changes files on disk, so the two writer examples overwrite their targets. The hard-coded paths noted above are specific to one machine; relative paths or paths assembled from the script's location make examples more portable.
