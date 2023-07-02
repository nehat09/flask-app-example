from flask import Flask

from server.views import books

def create_app():
	app = Flask(__name__)

	# register blueprints for APIs
	app.register_blueprint(books.bp)
	app.add_url_rule('/books', endpoint='books')

	@app.get("/")
	def version():
		return {"version": "0.1"}

	return app
