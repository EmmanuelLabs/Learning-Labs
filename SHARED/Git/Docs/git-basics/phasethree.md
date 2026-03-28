# GIT WORKFLOW CONTROL

## Stashing ( Temporary work preservation )

Core idea -- stash = temporary storage for unfinished work.

📌 What Problem It Solves:

You’re mid-work,
files modified
not ready to commit,
But you must
switch branches immediately.

Git blocks you to prevent data loss.

⚙️ What Happens Internally:

Working Directory → saved into stash

Staging Area      → saved into stash

Repo              → reset to last commit

Stored in:

refs/stash (stack structure)

🧠 Key Concepts:
stash is not permanent history, it
works like a stack (LIFO), and
does NOT include untracked files unless specified.

🧰 Core Commands:

git stash              # save changes
git stash -u           # include untracked files
git stash list         # view stashes
git stash apply        # restore without removing
git stash pop          # restore + remove
git stash drop         # delete specific 

⚠️ Critical Insight:

Stash stores changes, not commits.

💡 Real Use:

Interrupt → stash → switch → fix → return → restore.

## Cherry-Picking (Selective Commit Transfer)

🔑 Core Idea:

Cherry-pick = copy the effect of a commit.
NOT the commit itself.

📌 What Problem It Solves:

You need
ONE specific change,
But,
branch contains many commits (some broken).

⚙️ What Happens Internally:

Git
extracts the diff,
applies it to current branch, then
creates a new commit.

🧠 Key Concepts:

creates new commit (different hash),
original commit remains unchanged,
behaves like a mini-merge.

🧰 Core Commands

git cherry-pick <hash>
git cherry-pick A B C
git cherry-pick A^..C
git cherry-pick --continue
git cherry-pick --abort

⚠️ Why Conflicts Happen:

Change depends on original context,
Current branch may differ,
So Git cannot safely apply it.

💡 Real Use:

Extract hotfix → apply to production → avoid merging messy branch

## Interactive Rebase (History Rewriting)

🔑 Core Idea:

Rebase = replay commits.

Interactive = replay + edit them.

📌 What Problem It Solves:

Your history looks like
“fix”

“fix again”

“final fix”

Instead of:

“Implement feature”

⚙️ What Happens Internally:

Git
removes selected commits,
replays them one by one, while applying
your edits.

🧠 Key Concepts:

Interactive rebase,
rewrites history
changes commit hashes, and 
allows restructuring of commits.

🧰 Core Commands:

git rebase -i HEAD~n

🎛️ Rebase Actions:

pick    → keep
squash  → combine
reword  → edit message
edit    → modify commit
drop    → delete commit

⚠️ Golden Rule:

Never rebase shared/pushed commits.

💡 Real Use:

Clean messy development → present clean, logical history.

## Tags (Version Marking)

🔑 Core Idea:

Tag = permanent label for a commit.

📌 What Problem It Solves:

You need it to answer:
“Which version worked?”

⚙️ Types of Tags:

Lightweight:
git tag v1.0

Annotated (Recommended):

git tag -a v1.0 -m "Stable release"

🧠 Key Concepts:

Tags are fixed pointers. They
do NOT move like branches and
must be pushed manually.

🧰 Core Commands;

git tag
git tag -a v1.0 -m "message"
git show v1.0
git push origin v1.0
git push origin --tags

⚠️ Detached HEAD;

git checkout v1.0   # to view a specific tag 

You are not on a branch.

💡 Real Use of tags:

Mark releases → rollback → track milestones.

## PHASE 3 — BIG PICTURE
You now control:

🧩 Work State:

stash → pause work safely

🎯 Precision Changes:

cherry-pick → extract specific commits

🧹 History Quality:

interactive rebase → clean and structure 

📍 Version Control:

tags → mark stable points

## FINAL MENTAL MODEL

Working directory → active changes

Staging area      → prepared changes

Commit history    → permanent record

Stash             → temporary storage

Cherry-pick       → selective change copy

Rebase            → history rewrite

Tag               → fixed checkpoint

