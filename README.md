# flask-app-example

`flask-app-example` is a prototype for creating a REST API using Flask. This includes the API server, database connection to SQLite local database, tests and configuration for development and test run.

The API is designed to save a "Book" defined by `ID, Name, Author` as:

- `GET /api/books` - returns all books in database
- `POST /api/books` with JSON `{'name': '<bookname>', 'author': '<authorname>'}` - saves a Book record to database

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

Run tests in folder `tests` with `pytest`
```
python3 -m pytest tests
```

To run one test file, specify `path/to/testfile`
```
python3 -m pytest tests/functional/test_app.py
```

## What's Next?
- Add Build and Test (CI/CD) to the project
 