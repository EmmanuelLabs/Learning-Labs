# Lab 01: Git Initialization

# Objective:

To understand and use git for local version control and github for remote repository hosting.

# Tools Used:

Git (windows) , Git Bash, and GitHub (EmmanuelLabs account).

# STEP 1: Git Installation and Configuration

Installed Git version 2.52.0.windows.1

verified installation using  git --version

configured global username and email:
    git config --global user.name " My name "
	git config --global user.email " My email "

Purpose:
     To ensure all future commits are correctly attributed to the author.

# STEP 2: Repository Initialization

Initialized a local git repo using: git init < repo name > . In this case git init learning-labs .

Created initial Project structure:
    Docs/
	Lab/
	Asssets/
	Tools/

# STEP 3: First Commit

Created README.md

Staged it using: git add <file name> . In this case file name was README.md

Committed changes using: git commit -m " Initial commit: add project README "

# STEP 4: GitHub Integration

Created a remote repository on GitHub and called it: Learning-Labs

Linked local repo to remote: git remote add origin < repo-url >

Pushed commits to GitHub using: git push -u origin main 
    
	NOTE: By default, my local branch was *master. I confirmed this by typing git branch. 
	      I then renamed it main using git branch -m master main.
		  That's why git push -u origin main was able to run. 
		  Then went ahead and set main as a default branch on github by going to my learning-labs
		  repo, settings, branches then set main as the default branch. Then deleted the master branch on github.

# STEP 5:Error handling and corrections

Accidentally committed README.md twice

Learned thet Git tracks commit history, not file duplication.

Understood that identical files across commits do not create duplicates.

# Outcomes:

Successfully pushed a functional repository to github

Understood basic git workflow

Gained confidence in correcting mistakes.