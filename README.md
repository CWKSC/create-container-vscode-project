# create-container-vscode-project

This is a CLI tool automates the setup of a containerized VSCode project. It generates necessary files and commands for setting up a project within a Docker container for VSCode development.

## Install

Need to run under administrator permission

```bash
pip install create-container-vscode-project
```

## Usage

```bash
ccvp <project_name>
```

## Project Structure:

```
<project_name>/
|__ workspace/
|__ build.cmd
|__ Containerfile
|__ kill.cmd
|__ start.cmd
```

