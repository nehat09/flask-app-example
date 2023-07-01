# flask-app-example

`flask-app-example` is a prototype for creating a REST API using Flask. It includes writing the API code, writing tests with Test Driven Development and how to build and test the code.

## Install

Before installing this project, ensure Python is installed. Also, ensure you have referenced Flask Quickstart guide: https://flask.palletsprojects.com/en/2.3.x/installation/

Clone the project:
```
$ git clone https://github.com/nehat09/flask-app-example.git
```

Create and activate `virtualenv` (macOS):
```
$ python3 -m venv .venv
$ . .venv/bin/activate
```

Install dependencies with `pipenv`:
```
$ pip3 install pipenv
$ pipenv install
```

## Run

```
$ python3 -m app
```

In a browser, go to `http://localhost:5000`, the page should load JSON response with version.

## Test

Install `dev` dependencies
```
$ pipenv install --dev
```

Run tests with `pytest`
```
python3 -m pytest tests
```
