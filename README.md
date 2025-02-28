# How to Use This

## Prerequisites
- Ensure that python, pip, and npm are installed

## Run the Application

- Run these commands in a terminal to run the unit tests and backend locally (you may need to use "python3" instead of "python" depending on your device)

```sh 
cd backend
pip install flask flask-cors
python test_backend.py # Runs unit tests
python backend.py # Runs backend locally
```

- Leave the backend running in that terminal
- Next, open a new terminal and run this command to start the frontend (this might take some time)

```sh
python run_frontend.py
```

- Open a browser and navigate to http://localhost:4200/ to use the application
- Lastly, open a third terminal and run the E2E tests by running this command

```sh
python run_e2e.py
```

- In the new window, select E2E testing
- Select any browser and click "Start E2E Testing"
- In the new browser window, click the "spec.cy.ts" file and watch the tests automatically run
