# BRANCH COLLABORATION MECHANICS

## Branching Fundamentals.

A branch is just a pointer to a commit. A repository looks just like a chain of commits:
A -> B -> C 

Each commit stores:
 - snapshot of the project
- a reference to its parent

The branch name simply points to the latest commit. When you create a branch, Git does not DUPLICATE
YOUR FILES. It just creates another pointer. Both branches reference the same commit. When you commit
to the new branch, the histories diverge. That is:
    main = A to B to C
	branch ( feature-x ) = A to B to C to D

Important consequences:
    - branching is extremely cheap
	- you can create dozens of branches
	- switching branches rewrites your working directory to match that timeline.
	
	     So if a file exists only on feature-x, it disappears when you switch back to main.
		 Not deleted, just not part of that timeline.

# Merging Internals

Merging is combining two histories. Git performs a 3-way comparison. 

It looks at:
    1. the common ancestor
	2. branch A
	3. branch B

From our example histories above, C is the common ancestor. So Git calculates, changes in feature(branch) 
+ changes in main relative to C.

This leads to two outcomes:
    1. Fast-Forward Merge:
	    SCENARIO: 
		    main = A to B to C
			branch (feature-x) = A to B to C to D 
			
		Git simply moves the pointer, that is:
		    main = A to B to C to D 
			
		No merge commit. Just pointer movement.
	
	2. True Merge (3-way merge):
	    If both branches changed, that is;
		    main = A to B to C to D to E
			branch (feature-x) = A to B to C to F to G 
		
		Then Git creates a merge commit:
		    main = A to H, where H has two parents (E and G).
			
		This makes the git history look like (and is) a graph.
		
# Merge Conflicts

Merge conflicts happen when git cannot automatically combine changes from two branches.
Git merges automatically when edits occur in different files or different lines.

Conflicts occur when:
    - two branches modify the same lines
	- one branch deletes a file while another edits it
    - two branches rename the same file differently

Example history:
main = A to B to C to D
feature = A to B to C to E 

Both branches modify the same file line.
When you merge: git merge feature 
git stops and reports: CONFLICT (content): Merge conflict in docs/qos.md  Automatic merge failed

Now git inserts conflict markers into the file:

```

<<<<<<<< HEAD
QoS guarantees latency below 50ms
=========
QoS guarantees latency below 20ms
>>>>>>>> feature 
```

Meaning:
- HEAD = your current branch version
- feature = incoming branch version

You must manually edit the file to the correct final result:
    QoS guarantees latency below 20ms under optimized conditions

Then finalize the merge:
    git add docs/qos.md
	git commit

Git only finishes the merge after conflicts are resolved.

# Fetch, Pull, and Rebase

This section deals with synchronizing repositories across machines.
There are 3 separate operations.

GIT FETCH: 
    Fetch downloads new commits from the remote repository.
	It updates remote tracking branches but does not modify local branches

GIT PULL:
    Pull combines two operations, i.e git fetch + git merge.
	When run on main, git fetches remote commits and merges them into your branch.
	Your working branch updates automatically

GIT REBASE:
    Rebase integrates changes without creating a merge commit
	Rebase rewrites commit history
	Never rebase commits that were already pushed and shared

Golden Rule:
    Rebase local work
	Merge shared work

# Remote Branches and Tracking

Remote banches represent branches stored on remote servers.
Typical remote name: origin
Example listing: git branch -r 
Output:
    origin/main
	origin/login-feature
	origin/api-update 

These are remote-tracking branches.
They are read-only references representing the state of the remote repo.

Creating a tracking branch: use git switch branchname that is, git switch login-feature

Upstream tracking:
    The upstream brach tells Git where a local branch sends and receives updates
	Example command used is git push -u origin feature-x  where feature-x is the branch name
	The -u means set upstream branch/tracking
	After this, git push and git pull work automatically without specifying branch names

Inspecting remotes:
    git remote -v shows repository URLS

# Undoing Damage

Git provides multiple tools to reverse mistakes depending on where the mistake occurred.
Git architecture:
    working directory
	staging area 
	repository history 

Each undo command targets one of these layers.

GIT RESTORE:
    Restores files in the working directory. It discards local changes and restores last committed version.
	To restore a staged file, git restore --staged qos_notes.md  this removes the file from the staging area.
	
GIT RESET:
This moves the HEAD pointer to a different commit.
If your history is A B C D, and you run git reset HEAD~1, then your history becomes A B C, meaning
commit D is removed from the branch history.
Use git reset only when you've committed but not pushed yet.

Three reset modes exist.

soft reset;
    git reset --soft HEAD~1
	Undo commit but keep changes staged

mixed reset;
    git reset HEAD~1
	Undo commit and unstage changes

hard reset;
    git reset --hard HEAD~1
	Undo commit and delete all associated changes
	Dangerous but sometimes necessary

GIT REVERT:
    Revert does not delete history. Instead it creates a new commit that reverses a previous commit
	This is the prefered method in shared repositories.

# PHASE TWO COMMAND CHEAT SHEET

Essential commands learnt in this phase;
git merge
git fetch 
git pull 
git rebase 
git branch -r 
gir switch 
git switch -c 
git push -u 
git restore 
git reset 
git revert


