from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
	app = Flask(__name__)

	# config
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite'

	if test_config:
		app.config.update(test_config)

	# register blueprints for APIs
	from server.views import books

	app.register_blueprint(books.bp)
	app.add_url_rule('/books', endpoint='books')

	# initialize database
	db.init_app(app)
	with app.app_context():
		db.drop_all()
		db.create_all()

	@app.get('/')
	def version():
		return {'version': '0.1'}

	return app
