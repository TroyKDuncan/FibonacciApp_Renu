import subprocess
import os
import time
import sys


def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    process.communicate()


def open_new_terminal(command, cwd=None):
    if sys.platform == "darwin":  # macOS
        subprocess.Popen(
            ['osascript', '-e', f'tell application "Terminal" to do script "cd {cwd} && {command}"'])
    elif sys.platform == "win32":  # Windows
        subprocess.Popen(
            ['start', 'cmd', '/k', f'cd {cwd} && {command}'], shell=True)
    elif sys.platform == "linux":  # Linux
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c',
                         f'cd {cwd} && {command}; exec bash'])


def main():
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Ensure npm is installed
    try:
        subprocess.check_call(["npm", "--version"])
    except subprocess.CalledProcessError:
        print("npm is not installed. Please install Node.js and npm.")
        sys.exit(1)

    # Run backend unit tests
    print("Running backend unit tests...")
    backend_dir = os.path.join(project_root, "backend")
    run_command("npm install", cwd=backend_dir)
    run_command("npm test", cwd=backend_dir)

    # Run frontend unit tests
    print("Running frontend unit tests...")
    frontend_dir = os.path.join(project_root, "frontend")
    run_command("npm install", cwd=frontend_dir)
    run_command("npm test", cwd=frontend_dir)

    # Start backend in a new terminal
    print("Starting backend...")
    open_new_terminal("npm start", cwd=backend_dir)
    time.sleep(5)  # Wait for the backend to start

    # Start frontend in a new terminal
    print("Starting frontend...")
    open_new_terminal("npm start", cwd=frontend_dir)
    time.sleep(5)  # Wait for the frontend to start

    # Run Cypress e2e tests in a new terminal
    print("Running Cypress e2e tests...")
    open_new_terminal("npx cypress run", cwd=frontend_dir)


if __name__ == "__main__":
    main()
