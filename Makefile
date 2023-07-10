.PHONY: venv install run test clean

# default run start flask app
run: install
	.venv/bin/python3 -m app

venv:
	python3 -m venv .venv

install: venv
	.venv/bin/pip3 install pipenv
	.venv/bin/pipenv install

test:
	.venv/bin/pipenv install --dev
	.venv/bin/python3 -m pytest tests

clean:
	rm -rf .venv
	rm -rf instance
	rm -rf .pytest_cache
	find . -type f -name '*.pyc' -delete
