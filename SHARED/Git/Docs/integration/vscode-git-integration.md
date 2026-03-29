# VS Code + Git Integration
## Overview
Visual Studio Code provides a graphical interface for interacting with Git.

It allows you to perform common Git operations such as staging, committing, branching, and syncing without relying entirely on the terminal.

However, it does not replace Git. It only visualizes Git operations.
## Core Concepts
### Source Control Panel
The source control panel displays all changes in the current repository.

It shows:
- modified files
- staged files
- merge conflicts

This is equivalent to running `git status` in the terminal.

---
### Staging
Staging allows you to select specific changes before committing them.

In vs code:
- click the `+` icon to stage a file

Equivalent command:
```bash
git add filename
```
---
### Commit
A commit saves snapshot of your changes.

In vs code: 
- write a message
- click the checkmark (✓)

Equivalent command:
```bash
git commit -m "message"
```
---
### Sync (Push + Pull)
Sync combines pulling changes from the remote repository and pushing local changes.

Equivalent commands:
```bash
git pull
git push
```
---
### Branching
Branches allow you to work on features without affecting the main branch.

In vs code:
- click the branch name (bottom-left)
- create or switch branches

Equivalent command:
```bash
git switch -c branch-name
```
This creates a new branch and moves you to that branch.
---
### Conflict Resolution
When two branches modify the same parts of a file, Git creates a conflict.

Example:
```text
<<<<<<< HEAD (Current Change)
Version A
=======
Version B
>>>>>>> branch (Incoming Change)
```
VS Code provides options:
- Accept Current Change
- Accept Incoming Change
- Accept Both Changes

After resolving:
```bash
git add file
git commit
```
---
## Workflow Summary
Typical workflow:

1. Sync repository
2. Create or switch branch
3. Make changes
4. Review changes
5. Stage changes
6. Commit changes
7. Push to GitHub
8. Merge into main

## Key Takeaways
- VS Code simplifies Git operations through a graphical interface
- Understanding Git commands is still essential
- Branching helps manage changes safely
- Reviewig changes before committing is critical

