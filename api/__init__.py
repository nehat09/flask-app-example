from flask import Flask

def create_app():
	app = Flask(__name__)

	@app.get("/")
	def version():
		return {"version": "0.1"}

	return app
