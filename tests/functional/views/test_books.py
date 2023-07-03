import json

from server import db
from server.models.book import Book

def test_books_get(client):
	res = client.get('/api/books')
	assert res.status_code == 200
	assert 'books' in res.json

def test_books_post(app, client):
	testdata = {'name': 'test', 'author': 'pqr'}
	headers = {
    	'Content-type':'application/json', 
    	'Accept':'application/json'
	}
	res = client.post('/api/books', data=json.dumps(testdata), headers=headers)
	assert res.status_code == 201
	with app.app_context():
		select = db.select(db.func.count(Book.id))
		post_count = db.session.execute(select).scalar()
		assert post_count == 3