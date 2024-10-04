import subprocess
import sys
from pathlib import Path

def save_to_file(content, project_name, filename):
    with open(Path(project_name) / filename, 'w') as file:
        file.write(content)

def generate_build_develop_cmd(project_name):
    content = f"""docker image build . `
    --file ./Containerfile.develop `
    --tag {project_name}-develop-image
"""
    save_to_file(content, project_name, "build.develop.ps1")

def generate_build_release_cmd(project_name):
    content = f"""docker image build . `
    --file ./Containerfile.release `
    --pull=false `
    --tag {project_name}-release-image
"""
    save_to_file(content, project_name, "build.release.ps1")

def generate_develop_containerfile(project_name):
    content = f"""FROM docker.io/python:latest

RUN pip install --upgrade pip

"""
    save_to_file(content, project_name, "Containerfile.develop")

def generate_release_containerfile(project_name):
    content = f"""FROM {project_name}-develop-image

COPY ./workspace /workspace

"""
    save_to_file(content, project_name, "Containerfile.release")

def generate_develop_start_cmd(project_name):
    container_name = f"{project_name}-develop-container"
    container_name_hex = container_name.encode('ascii').hex()
    content = f"""docker container run `
    --detach `
    --hostname "{container_name}" `
    --interactive `
    --name "{container_name}" `
    --rm `
    --stop-timeout 0 `
    --tty `
    --volume "$PWD/workspace/:/workspace/" `
    {project_name}-develop-image

if (Get-Command "cursor" -errorAction SilentlyContinue)
{{
    cursor --folder-uri vscode-remote://attached-container+{container_name_hex}/workspace
}}
elseif (Get-Command "code" -errorAction SilentlyContinue)
{{
    code --folder-uri vscode-remote://attached-container+{container_name_hex}/workspace
}}

"""
    save_to_file(content, project_name, "start.develop.ps1")

def generate_release_start_cmd(project_name):
    container_name = f"{project_name}-release-container"
    content = f"""docker container run `
    --hostname "{container_name}" `
    --name "{container_name}" `
    --rm `
    {project_name}-release-image
"""
    save_to_file(content, project_name, "start.release.ps1")

def generate_develop_kill_cmd(project_name):
    content = f"docker container kill {project_name}-develop-container"
    save_to_file(content, project_name, "kill.develop.ps1")

def generate_release_kill_cmd(project_name):
    content = f"docker container kill {project_name}-release-container"
    save_to_file(content, project_name, "kill.release.ps1")

def setup_project(project_name):
    project_dir = Path(project_name)
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "workspace").mkdir(exist_ok=True)
    
    generate_develop_containerfile(project_name)
    generate_release_containerfile(project_name)
    generate_build_develop_cmd(project_name)
    generate_build_release_cmd(project_name)
    generate_develop_start_cmd(project_name)
    generate_release_start_cmd(project_name)
    generate_develop_kill_cmd(project_name)
    generate_release_kill_cmd(project_name)

    print("Project setup completed.")

def main():
    if len(sys.argv) != 2:
        print("Usage: ccvp <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    setup_project(project_name)

if __name__ == "__main__":
    main()

