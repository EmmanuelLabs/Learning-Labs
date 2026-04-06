# VS Code Integration (Python Extension)
## Overview
To enable efficient Python development, Visual Studio Code was configured with the official Python extension, allowing the editor to understand, execute, and assist with Python code.
## Step 1 — Install Python Extension
1. Open VS Code
2. Navigate to Extensions panel:
```Plain text
Ctrl + Shift + X
```
3. Search for:
```Plain text
Python
```
4. Install:
```Plain text
Python (by Microsoft)
```
## Step 2 — Select Python Interpreter
1. Open Command Palette:
```Plain text
Ctrl + Shift + P
```
2. Search:
```Plain text
Python: Select Interpreter
```
3. Select:
```Plain text
Python 3.12.9 (C:\Dev\Python312\...)
```
## Step 3 — Verify Integration
1. Create a test file:
```Plain text
test.py
```
2. Add code:
```Python
print("VS Code is working")
```
3. Run using:
- Run button (top right), or
- Right-click → Run Python File
## Outcome
- Python code executes successfully within VS Code
- Syntax highlighting is active
- No interpreter-related errors
