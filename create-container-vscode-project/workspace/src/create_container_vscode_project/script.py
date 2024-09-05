import subprocess
import sys
from pathlib import Path

def generate_containerfile(project_name):
    content = f"""FROM docker.io/python:latest

RUN pip install --upgrade pip

"""
    save_to_file(content, project_name, "Containerfile")

def generate_build_cmd(project_name):
    content = f"""docker image build . ^
    --file ./Containerfile ^
    --tag {project_name}-image"""
    save_to_file(content, project_name, "build.cmd")

def generate_start_cmd(project_name):
    container_name = f"{project_name}-container"
    container_name_hex = container_name.encode('ascii').hex()
    content = f"""docker container run ^
    --detach ^
    --hostname "{container_name}" ^
    --interactive ^
    --name "{container_name}" ^
    --privileged ^
    --rm ^
    --stop-timeout 0 ^
    --tty ^
    --volume "%cd%/workspace/:/workspace/" ^
    --gpus all ^
    {project_name}-image

code --folder-uri vscode-remote://attached-container+{container_name_hex}/workspace
"""
    save_to_file(content, project_name, "start.cmd")

def generate_kill_cmd(project_name):
    content = f"docker container kill {project_name}-container"
    save_to_file(content, project_name, "kill.cmd")

def save_to_file(content, project_name, filename):
    with open(Path(project_name) / filename, 'w') as file:
        file.write(content)

def setup_project(project_name):
    project_dir = Path(project_name)
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "workspace").mkdir(exist_ok=True)
    
    generate_containerfile(project_name)
    generate_build_cmd(project_name)
    generate_start_cmd(project_name)
    generate_kill_cmd(project_name)

    print("Project setup completed.")

def main():
    if len(sys.argv) != 2:
        print("Usage: ccvp <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    setup_project(project_name)

if __name__ == "__main__":
    main()

