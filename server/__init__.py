from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

from server import config

logging.basicConfig(
	level=logging.DEBUG,
	format='[%(asctime)s] %(levelname)s: %(message)s'
)

logger = logging.getLogger(__name__)
db = SQLAlchemy()


def create_app(config=config.DevelopmentConfig):
	app = Flask(__name__)

	# get configuration from config object
	app.config.from_object(config)

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

	logger.info('Flask app initialized')
	return app
