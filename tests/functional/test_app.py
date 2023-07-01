def test_api_health(app, client):
	res = client.get("/")
	assert res.status_code == 200
