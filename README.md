# Instructions for setup

- To run the project you'll need both python and node js installed, you can find out more at:
  - https://www.python.org/getit/ 
  - https://nodejs.org/en/download/

## Run locally

- After cloning the repository you'll need to run the Flask API server and the Vue JS frontend server.

### Start Flask Server

- Create a new .env file in the same directory as env_example.txt and copy the settings variables from env_example.txt to the new .env file, debug settings and the app secret key can be set.

- Create a python virtual environment in order to run the Flask API server, and activate it. Information on how to create and activate a python virtual environment can be found at <https://docs.python.org/3/tutorial/venv.html>.

- Install the requirements by running:

```
$ pip install -r requirements.txt
```

- Run this command to start the server.

```
$ python app.py
```

- The Flask server should start running at <http://0.0.0.0:5000/>, the API is accessible through <http://0.0.0.0:5000/interactions/api>.

### Start Vue JS App

- Go to the frontend directory in the project.

- Install packages by running:

```
$ npm install
```
- Run the Vue JS app by running:

```
$ npm run serve
```
- The app will start running at <http://localhost:8080/>

- Both the Flask server and Vue JS server will need to run for the project to work.
