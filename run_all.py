import subprocess
import os
import time


def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    process.communicate()


def main():
    project_root = "/Users/troyduncan/projects/FibApp_Renu/FibonacciApp_Renu"

    # Run backend
    print("Starting backend...")
    backend_dir = os.path.join(project_root, "backend")
    run_command("npm install", cwd=backend_dir)
    run_command("npm start", cwd=backend_dir)
    time.sleep(5)  # Wait for the backend to start

    # Run backend unit tests
    print("Running backend unit tests...")
    run_command("npm test", cwd=backend_dir)

    # Run frontend
    print("Starting frontend...")
    frontend_dir = os.path.join(project_root, "frontend")
    run_command("npm install", cwd=frontend_dir)
    run_command("npm start", cwd=frontend_dir)
    time.sleep(5)  # Wait for the frontend to start

    # Run frontend unit tests
    print("Running frontend unit tests...")
    run_command("npm test", cwd=frontend_dir)

    # Run Cypress e2e tests
    print("Running Cypress e2e tests...")
    run_command("npx cypress install", cwd=frontend_dir)
    run_command("npx cypress run", cwd=frontend_dir)


if __name__ == "__main__":
    main()
