import pytest

from server import create_app, db
from server.models.book import Book

@pytest.fixture
def app():
	flask_app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})

	with flask_app.app_context():
		db.create_all()
		db.session.add_all(
            (
                Book(name='test1', author='abc'),
                Book(name='test2', author='pqr')
            )
        )
		db.session.commit()
	
	yield flask_app

@pytest.fixture
def client(app):
	return app.test_client()
