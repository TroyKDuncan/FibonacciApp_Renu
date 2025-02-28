import subprocess
import os


def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    process.communicate()


def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(project_root, "frontend")

    # Run Cypress end-to-end tests
    print("Running Cypress end-to-end tests...")
    run_command("npm run e2e", cwd=frontend_dir)


if __name__ == "__main__":
    main()
