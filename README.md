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
|__ build.ps1
|__ Containerfile
|__ kill.ps1
|__ start.ps1
```

Powershell (`.ps1`) is cross-platform, this why I use it


