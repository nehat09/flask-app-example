import pytest

from server import create_app

@pytest.fixture
def app():
	flask_app = create_app()
	yield flask_app

@pytest.fixture
def client(app):
	return app.test_client()
