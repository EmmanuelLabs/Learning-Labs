# Python Setup — Windows (v3.12.9)
## Overview
This document describes the complete installation and configuration of Python on a Windows system, ensuring it is properly integrated into the system environment and ready for development, scripting, and automation tasks.
## Version Selection
- Installed Version: Python 3.12.9 (64-bit)
- Source: [Download here](https://www.python.org/downloads/windows)

> **Rationale:**
> - Stable and widely supported
> - Compatible with most libraries and tools
> - Avoids issues associated with newly released versions
## Installation Process
### Step 1 — Download Installer
---
- Navigated to official Python downloads page
- Downloaded:
```Plain text
Windows Installer (64-bit)
```
### Step 2 — Launch Installer
---
- Executed the installer file
 #### Critical Options Selected:
-  Add Python to PATH
-  Use admin privileges when installing py.exe

### Step 3 — Customize Installation
Selected “**Customize Installation**” instead of default install.
### Step 4 — Optional Features
All default options were selected:

✔ pip (package manager)

✔ tcl/tk (GUI support)

✔ documentation

✔ standard libraries
### Step 5 — Advanced Options
Configured as follows:

✔ Install for all users

✔ Add Python to environment variables

✔ Precompile standard library

Installation Directory:
```Plain text
C:\Dev\Python312\
```
### Step 6 — Excluded Components
The following options were intentionally NOT selected:

❌ Download debugging symbols

❌ Download debug binaries

#### Reason:
- Not required for standard development or scripting
- Intended for low-level debugging and Python internals
## Installation Verification
### Step 1 — Verify Python 
---
Opened Command Prompt and executed:
````Bash
python --version
````
Output:
`````Plain text
Python 3.12.9
`````
### Step 2 — Verify pip Installation
---
```Bash
pip --version
```
#### Confirms:
- pip is installed and accessible
- Python package management is functional
### Step 3 — Test Python Interpreter
```Bash
python
```
Then executed:
```Python
print("Hello, engineer")
```
Output:
```Plain text
Hello, engineer
```
Exit interpreter:
```Bash
exit()
``` 
### Step 4 — Verify Python Launcher (py.exe)
---

```Bash
py --version
```
#### Confirms:
- Python Launcher is installed
- Multiple Python versions can be managed if needed
## Environment Validation
Python is considered correctly configured if:
- python command works globally
- pip command is accessible
- py launcher responds correctly
- No “not recognized as internal or external command” errors
## System Integration
#### PATH Configuration
Python was successfully added to system PATH, enabling:
```Bash
python
pip
py
```
to be executed from any directory.
#### Installation Scope
- Installed system-wide (all users)
Located in:
```Plain text
C:\Dev\Python312\
```
## Common Issues (Prevented)
|Issue | Prevention |
|------ |------ |
|Python not recognized | Added to PATH during install
|Permission issues | Installed with admin previledges
|Version conflicts | Used stable version (3.12.9)
|Missing pip | Included in optional features
## Outcome
Python is fully installed, configured, and ready for:
- scripting
- automation
- networking tools
- software development
- integration with VS Code and Git workflows
## Next Steps
- Install Python extensions in VS Code
- Begin structured learning (separate workflow)
- Use Python within Git-tracked projects
