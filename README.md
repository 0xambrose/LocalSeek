# LocalSeek

A powerful command-line tool for searching files and content on your local filesystem.

## Features

- **File Name Search**: Find files by name using wildcard patterns
- **Content Search**: Search inside file contents with text or regex patterns
- **File Extension Filtering**: Filter results by specific file extensions
- **Syntax Highlighting**: Highlight search matches in terminal output
- **Cross-platform**: Works on Linux, macOS, and Windows

## Installation

```bash
pip install localseek
```

## Usage

### Search by file name
```bash
localseek -p "*.py"              # Find all Python files
localseek -p "*config*"          # Find files containing "config"
localseek -p "test_*.py"         # Find test files
```

### Search file contents
```bash
localseek -p "TODO" -c           # Search for "TODO" in file contents
localseek -p "function.*main" -c -r    # Regex search for function definitions
localseek -p "import" -c -e py   # Search Python files for "import"
```

### Filter by file extensions
```bash
localseek -p "class" -c -e py -e js    # Search in Python and JS files
localseek -p "*" -e txt -e md          # Find all text and markdown files
```

### Options
- `-p, --pattern`: Search pattern (required)
- `-c, --content`: Search file contents instead of names
- `-r, --regex`: Use regex for content search
- `-e, --ext`: Filter by file extensions
- `--path`: Search path (default: current directory)
- `--no-highlight`: Disable search result highlighting

## Examples

```bash
# Find configuration files
localseek -p "*config*"

# Search for Python classes
localseek -p "class.*:" -c -r -e py

# Find TODO comments in source files
localseek -p "TODO" -c -e py -e js -e cpp

# Search for function definitions in current directory
localseek -p "def " -c --path ./src
```