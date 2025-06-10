# File Manager Project
This program provides a simple way to manage and manipulate text files using Python. It includes two classes, FileManager and MultiFileManager and ...


## Setup and Run


### 1. Create and Activate Virtual Environment
If you haven’t already created a virtual environment, run the following command:

```bash
python3 -m venv venv
```

#### Activate the Virtual Environment:

To activate the environment, use the following command:

```bash
source venv/bin/activate
```

### 2. Install Dependencies
Install the required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 3. Run Tests
Use pytest to execute the tests:

```bash
PYTHONPATH=. pytest
```
This command ensures that Python includes the correct project paths when running the tests.


## Key Features

Below is an example of how to use the key features of the FileManager and MultiFileManager classes:

```py
# Importing classes
from file_manager.manager import FileManager, MultiFileManager

# Example 1: Create a FileManager for a file
file1 = FileManager("example1.txt")
file2 = FileManager("example2.txt")

# Read the file line by line
print("Lines in example1.txt:")
for line in file1.lines():
    print(line)

# Example 2: Check file size
print(f"Size of example1.txt: {FileManager.file_size('example1.txt')} bytes")

# Example 3: Combine two files with +
combined_file = file1 + file2
print(f"Combined file created: {combined_file.path}")

# Example 4: Create FileManager from a directory and file name
file_from_dir = FileManager.from_dir(".", "example1.txt")
print(f"Created FileManager from directory: {file_from_dir}")

# Example 5: Use MultiFileManager to combine many files
multi_manager = MultiFileManager("example1.txt")
final_combined = multi_manager.concat_many("example2.txt", "example3.txt")
print(f"Final combined file created: {final_combined.path}")

# Example 6: Pretty printing
print(file1)  # FileManager output
print(multi_manager)  # MultiFileManager output (in red)
```

### What This Does

#### Reads lines from example1.txt.

#### Checks the size of example1.txt.

#### Combines example1.txt and example2.txt into a new file.

#### Creates a FileManager object directly from a directory.

#### Combines multiple files (example1.txt, example2.txt, example3.txt) into one using MultiFileManager.

#### Prints details of the files with added color for MultiFileManager.
