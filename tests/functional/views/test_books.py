import json

from server import db
from server.models.book import Book

HEADERS = {
    'Content-type':'application/json', 
	'Accept':'application/json'
}


def test_books_get(client):
	res = client.get('/api/books')
	assert res.status_code == 200
	assert 'books' in res.json


def test_books_post(app, client):
	testdata = {'name': 'test', 'author': 'pqr'}
	res = client.post('/api/books', data=json.dumps(testdata), headers=HEADERS)
	assert res.status_code == 201
	with app.app_context():
		select = db.select(db.func.count(Book.id))
		post_count = db.session.execute(select).scalar()
		assert post_count == 3


def test_books_post_error_400(client):
	res = client.post('/api/books', data=[], headers=HEADERS)
	assert res.status_code == 400


def test_books_post_error_415(client):
	res = client.post('/api/books', data=[])
	assert res.status_code == 415


def test_books_post_error_500(client):
	testdata = {'name': 'samebook', 'author': 'pqr'}
	res1 = client.post('/api/books', data=json.dumps(testdata), headers=HEADERS)
	res2 = client.post('/api/books', data=json.dumps(testdata), headers=HEADERS)
	assert res1.status_code == 201
	assert res2.status_code == 500
