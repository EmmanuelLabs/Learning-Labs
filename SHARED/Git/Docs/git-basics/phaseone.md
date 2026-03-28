# Git Basics Phaseone

## What I Thought Before

Nothing. I had no idea of what git was. All I knew from all the youtube and tiktok DevOps engineering and software development roadmaps was that learning git for version control should be your first step. 

## What I Learned

Apparently, this thing is what developers use to track changes and maybe troubleshoot problems in their work.
Git just takes snapshots of your work or different versions of them and stores them locally in your machine until you push them to cloud (GIT HUB). 
Another thing i've learnt about git, it is very different from github. I already had prior knowledge of github 
and so, learning about git, i thought they might be related somehow. As of the knowledge that I HAVE RIGHT now, these two things are not the same 
but they work together. We first do everything in git, and once we are sure about everything, we can push them to git hub for the public to see.

Git has 3 main areas, or parts. Working tree, staging area and commit. We start with the working tree where we do everything and anything as long as we are in the local repository path, where git can track and notify us about changes in our files.
This is where we create, modify and even delete files( not sure yet about deleting). Once done, we add these new files and the modified files to the staging area
before committing them to the local local repo. At the staging area, we can decide which versions to permanently store (commit), and remove the remaining ones if
they were too many. Last step to store the files in your machine, that is, commit to local repo. During commit, you write a small message of what that file represents, or if it's a
modified version of an existing file that maybe fixes a specific bug, you specify it, to later make your work easier while troubleshooting an unknown issue.

## Why it Matters

Understanding basic git workflow, has given me the courage to use git freely without the fear of commiting the wrong file, 
or modifying files. With the workflow, i can modify my files in different ways and stage them, then later, review them before commiting to make sure i only store the ones that matter.

## Commands Involved

git config --global

git status

git init

pwd

git add 

git commit -machine

git push

## Open questions

As of now, this is a new thing for me. I have very many questions that need answers, but i'm confident i'll get the answers as i move forward.
Fro this phase though, one thing is still bothering me, what was the purpose of git config,
why was the first step that i needed to learn and apparently only need to do it once in any machine setting up my username and my email password.
At first, i was even dumb enough to think that it helps git track your progress accross diferent machines. THAT'S NOT THE CASE. Git clone helps git track my progress accross different machines.
