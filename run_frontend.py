import subprocess
import os


def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    process.communicate()


def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(project_root, "frontend")

    # Install dependencies
    print("Installing frontend dependencies...")
    run_command("npm install", cwd=frontend_dir)

    # Start the frontend server
    print("Starting frontend server...")
    run_command("npm run start", cwd=frontend_dir)


if __name__ == "__main__":
    main()
