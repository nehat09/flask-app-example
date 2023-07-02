def test_books_get(client):
	res = client.get("/api/books")
	assert res.status_code == 200
	assert 'books' in res.json