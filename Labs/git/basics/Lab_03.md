# LAB 03: GIT RECOVERY AND DAMAGE CONTROL.

This lab simulates a real repository accident.
Scenario:
A developer commits something incorrect.
The bad commit gets pushed to GitHub.
Files are accidentally deleted.
The team must recover using revert, reset, restore, and reflog.
No toy examples here. This is the sort of mess that happens in actual repositories.
Lab 03 — Git Recovery and Damage Control
Objective
The objective of this lab is to understand how Git handles mistakes in a repository and how developers can safely recover from them. The experiment demonstrates methods for undoing incorrect commits, restoring deleted files, and reversing changes that have already been pushed to a remote repository.
Step 1 — Prepare the Repository
Navigate into your repository.
Bash
cd your-repo-name
Make sure everything is synchronized.
Bash
git pull
Now create a new file that will simulate a configuration file.
Bash
echo "API_ENDPOINT=192.168.1.10" > config.env
Stage and commit.
Bash
git add config.env
git commit -m "Add configuration file"
Push to GitHub.
Bash
git push
Repository state:

A → B → C
Step 2 — Simulate a Bad Commit
Now simulate a common mistake: committing sensitive data.
Edit config.env.

API_ENDPOINT=192.168.1.10
API_KEY=123456789SECRET
Stage and commit.
Bash
git add config.env
git commit -m "Add API key for testing"
Push it.
Bash
git push
Now the bad commit is already published.
This happens more often than anyone wants to admit.
Step 3 — Fix the Problem Using Revert
Because the commit is already pushed, reset is unsafe. It rewrites history.
Instead use:
Bash
git revert HEAD
Git creates a new commit that removes the change.
History becomes:

A → B → C → D → E
Where:

D = bad commit
E = revert commit
Push the correction.
Bash
git push
The secret is now removed without rewriting history.
(And in real life you'd rotate the key immediately.)
Step 4 — Simulate Accidental File Deletion
Now simulate another mistake.
Delete the configuration file.
Bash
rm config.env
Check repository status.
Bash
git status
Git will show:

deleted: config.env
Commit the deletion accidentally.
Bash
git add config.env
git commit -m "Remove config file"
git push
Now the file is gone.
Step 5 — Recover the Deleted File
First inspect the commit history.
Bash
git log
Find the commit that still contained the file.
Now restore it.
Bash
git checkout HEAD~1 -- config.env
This command retrieves the file from the previous commit.
Stage and commit the restoration.
Bash
git add config.env
git commit -m "Restore deleted configuration file"
Push the fix.
Bash
git push
File recovered.
No panic necessary.
Step 6 — Inspect History Using Reflog
Git internally tracks every movement of the HEAD pointer.
This log is called reflog.
Run:
Bash
git reflog
You’ll see entries like:

HEAD@{0}: commit: Restore deleted configuration file
HEAD@{1}: commit: Remove config file
HEAD@{2}: revert: Revert "Add API key for testing"
HEAD@{3}: commit: Add API key for testing
Reflog is Git’s black box recorder.
Even if commits disappear from history, reflog can often recover them.
Step 7 — Restore a Previous State Using Reset (Local Only)
Now simulate fixing a mistake before pushing.
Create a test commit.
Bash
echo "debug=true" >> config.env
git add config.env
git commit -m "Temporary debug setting"
Now decide that commit should never exist.
Undo it locally.
Bash
git reset --soft HEAD~1
The commit disappears but the changes remain staged.
If you want to discard everything completely:
Bash
git reset --hard HEAD~1
That removes both the commit and its changes.
Skills Practiced in Lab 03
This lab demonstrated critical Git recovery techniques:
reversing a pushed commit using git revert
restoring deleted files from previous commits
examining history using git log
using git reflog to track repository history
undoing local commits with git reset
recovering files from earlier commits
These skills are essential for maintaining repository integrity in collaborative projects.
What Makes This Lab Realistic
These are actual industry mistakes:
committing sensitive credentials
pushing incorrect commits
deleting important files
needing to recover history
Developers encounter these situations constantly.
Git’s design ensures that almost every mistake can be recovered if the correct commands are used.
Conclusion
The lab demonstrated how Git provides multiple mechanisms for recovering from mistakes in a repository. While incorrect commits and file deletions may occur during development, tools such as revert, restore, reset, and reflog allow developers to safely reverse or recover these changes.
Understanding these recovery mechanisms is essential for managing repositories in collaborative development environments and for maintaining a reliable version history.
You’ve now completed Phase 2 labs, which means you’ve practiced the core workflows behind professional Git usage:
branching
merging
remote synchronization
conflict resolution
repository recovery
Next comes Phase 3, where Git starts behaving less like a version control system and more like a precision surgery toolkit for commits.
That’s where you learn things many developers never bother mastering:
stashing work temporarily
cherry-picking commits between branches
interactive rebase (history rewriting like a surgeon)
And that’s the moment Git stops feeling mysterious and starts feeling dangerously powerful.