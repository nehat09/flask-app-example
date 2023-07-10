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

This project uses `make` as a build tool. _Why?_ - `make` _makes it easier to build/test/run your project which is useful for development, as well as running builds in deployments (CI/CD)._

## Run
Run the app with `make run` or just `make`(default). This will start up the flask app on `localhost:5000`:
```
make run
```
In a browser, go to `localhost:5000`, should load a JSON response with version.

## Test
Run all tests:
```
make test
```

Run a specific test file with `pytest path/to/testfile`
```
python3 -m pytest tests/functional/test_app.py
```


Run `make clean` to cleanup the project folder, deleting any files generated during development.

---

**What's Next?**
- Add Kubernetes CI/CD to the project
