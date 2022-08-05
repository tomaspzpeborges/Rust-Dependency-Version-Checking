# Rust Dependency Checking


This project uses a new command line tool to update a dependency tree of a Rust project.
Developed for the 8-hour World's ARM Interns Hackathon 2022. This project achieved 2nd place in best execution.

## How to use: 

python3 script.py -a parsec -c parsec-tool


## About the functionality: 

This tool takes two mandatory command line arguments, -a (anchor project) and -c (comparable project). We assumed that one of the projects will take precedence over the other, and then we only update the preferences of the second one. Then, the script looks for the two projects and checks if they are written in rust. If so, we get the dependency trees by running cargo tree. 

Raw output from 'cargo tree' is parsed into a tree structure and we do so for both projects. The tree for the anchor project is parsed first so we can build the hash map of all the dependencies used. Then, we parse the second tree and check against common dependencies; for each found, we update it with the corresponding latest dependecy version in the anchor project. Lastly, we output a tree highlighting the diff between the original one and the updated.

The tool was also designed to takes an optional argument --build, to run cargo build on the updated project. This is currently not implemented but is a possible point of future development. 

