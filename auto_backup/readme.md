# File Backup Utility

A simple Python utility for creating dated backups of files. This script allows you to easily create backup copies of files with timestamps in their names.

## Features

- Automatically adds date prefix to backup files
- Configurable source and destination directories
- Custom naming support for backup files
- Error handling for common file operations
- Cross-platform compatibility

## Installation

No additional packages are required beyond Python's standard library.

```bash
git clone https://your-repository/backup-utility.git
cd backup-utility
```

## Usage

### Basic Usage

```python
from backup_utility import take_backup

# Create a backup of 'GFG.txt' in the './backups/' directory
take_backup("GFG.txt")
```

### Advanced Usage

```python
# Backup with custom destination filename and directory
take_backup(
    src_file_name="data.csv",
    dst_file_name="important_data.csv",
    src_dir="./data/",
    dst_dir="important_backups/"
)
```

### Parameters

- `src_file_name` (str): Name of the file to backup (required)
- `dst_file_name` (str, optional): Custom name for the backup file. If not provided, uses date prefix with original filename
- `src_dir` (str, optional): Source directory path. Defaults to './'
- `dst_dir` (str, optional): Destination directory path. Defaults to './backups/'

### Output Format

When no destination filename is provided, backup files are named in the format:
`DD_Mon_YYYY_original_filename`

Example: `12_Nov_2024_GFG.txt`

## Error Handling

The utility handles common errors including:

- Missing source files
- Insufficient permissions
- Invalid paths

## Examples

```python
# Basic backup
take_backup("GFG.txt")  # Creates: backups/12_Nov_2024_GFG.txt

# Backup with custom name and directory
take_backup(
    "data.csv",
    "important_data.csv",
    dst_dir="important_backups/"
)  # Creates: important_backups/important_data.csv
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

Apache Licence, v2.0
