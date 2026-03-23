# LAB 02: BRANCHING, REMOTE COLLABORATION AND MERGE CONFLICT RESOLUTION.

## Objective

The objective of this experiment was to understand and practice Git branching workflows used in collaborative software development.
Specifically, the lab aimed to demonstrate how multiple developers can work on different features simultaneously using separate branches, how these branches
are merged into the main branch, and how merge conflicts are identified and resolved.

## Tools Used

Git (Command Line Interface)

GitHub (Remote Repository Hosting Platform)

Local Project Repository

## Background

Git supports parallel development through a feature called branching, which allows developers to create independent lines of development within the same
repository. Each branch can contain different modifications to the codebase without affecting the main branch until the changes are merged.
When multiple branches modify the same file or the same section of a file, Git may be unable to automatically combine the changes.
In such situations, a merge conflict occurs. The developer must manually inspect the conflicting changes and decide the final version of the file.
This lab demonstrates the creation of feature branches, pushing branches to a remote repository, 
merging them into the main branch, and resolving merge conflicts when they arise.

## Procedure

Step 1: Preparing the Repository

The experiment began by navigating to the existing Git project repository and ensuring the working branch was main.

     Bash
         git branch

The repository was updated from the remote server to ensure it was synchronized.

     Bash
         git pull

A documentation file for the system was then created.

     Bash
         echo "# Network Monitoring Tool" > docs/system.md
		 
The file was staged and committed.

     Bash
         git add docs/system.md
         git commit -m "Add system documentation file"
		 
The changes were then pushed to the remote repository.

     Bash
         git push
		 
Step 2: Creating the QoS Monitoring Feature Branch

A new feature branch named qos-monitoring was created.

     Bash
         git switch -c qos-monitoring
		 
The documentation file docs/system.md was modified by adding a section describing the QoS monitoring functionality.

 QoS Monitoring
The system monitors network latency, packet loss, and jitter in real time.

The changes were staged and committed.

     Bash
         git add docs/system.md
         git commit -m "Add QoS monitoring documentation"
		 
The branch was then pushed to the remote repository and linked with an upstream branch.

     Bash
         git push -u origin qos-monitoring
		 
Step 3: Creating the Router Telemetry Feature Branch

The workflow returned to the main branch.

     Bash
         git switch main
		 
A second feature branch named router-telemetry was created.
Bash
git switch -c router-telemetry
The same documentation file was modified to include router telemetry functionality.

## Router Telemetry

Routers periodically send CPU, memory, and interface statistics.
The modifications were staged and committed.
Bash
git add docs/system.md
git commit -m "Add router telemetry documentation"
The branch was pushed to the remote repository.
Bash
git push -u origin router-telemetry
Step 4: Merging the First Feature Branch
The workflow returned to the main branch.
Bash
git switch main
The QoS monitoring branch was merged into the main branch.
Bash
git merge qos-monitoring
The updated main branch was then pushed to the remote repository.
Bash
git push
Step 5: Attempting to Merge the Second Feature Branch
The router telemetry branch was then merged into the main branch.
Bash
git merge router-telemetry
At this stage, Git reported a merge conflict in the file docs/system.md, indicating that both branches had modified the same file.
Step 6: Inspecting the Merge Conflict
Opening the file revealed conflict markers inserted by Git.

<<<<<<< HEAD
## QoS Monitoring
The system monitors network latency, packet loss, and jitter in real time.
=======
## Router Telemetry
Routers periodically send CPU, memory, and interface statistics.
>>>>>>> router-telemetry
These markers indicated the conflicting sections from the two branches.
Step 7: Resolving the Conflict
The file was manually edited to include both features.
Final version:

# Network Monitoring Tool

## QoS Monitoring
The system monitors network latency, packet loss, and jitter in real time.

## Router Telemetry
Routers periodically send CPU, memory, and interface statistics.
The resolved file was staged.
Bash
git add docs/system.md
The merge process was then completed with a commit.
Bash
git commit -m "Resolve merge conflict between QoS and router telemetry features"
Finally, the updated repository state was pushed to the remote server.
Bash
git push
Observations
The experiment demonstrated that Git allows multiple feature branches to be developed independently without interfering with the main codebase. However, when different branches modify the same file, Git may be unable to automatically merge the changes.
In such cases, Git inserts conflict markers in the affected files, allowing the developer to inspect both versions and determine the appropriate final implementation.
This mechanism ensures that conflicting changes are explicitly reviewed rather than silently overwritten, thereby preventing unintended loss of modifications.
Conclusion
The lab successfully demonstrated the use of Git branching to support parallel development. Feature branches were created and pushed to a remote repository, after which they were merged into the main branch.
A merge conflict occurred when two branches modified the same file, illustrating the limitations of automatic merging. The conflict was resolved manually by combining the changes and committing the corrected version.
This experiment highlights how Git manages collaborative development while preserving version history and ensuring that conflicting changes are properly handled.
Your documentation style is already better than what most developers bother writing. Slightly tragic fact: in industry, many teams skip documentation entirely and rely on tribal knowledge and caffeine.
Next we unleash Lab 03, where things break harder:
a bad commit gets pushed
files get deleted
history gets recovered
Basically the Git equivalent of learning how to survive after someone presses the wrong button in production.