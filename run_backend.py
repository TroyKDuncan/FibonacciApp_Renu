import subprocess
import os


def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    process.communicate()


def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(project_root, "backend")

    # Ensure Flask and flask-cors are installed
    print("Installing Flask and flask-cors...")
    run_command("pip install flask flask-cors", cwd=backend_dir)

    # Run the unit tests
    print("\nRunning backend unit tests...")
    run_command("python test_backend.py", cwd=backend_dir)

    # Start the backend server
    print("Starting backend server...")
    run_command("python backend.py", cwd=backend_dir)


if __name__ == "__main__":
    main()
