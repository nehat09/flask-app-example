from flask import Blueprint
from flask import request, jsonify
from sqlalchemy.exc import SQLAlchemyError

from server import db
from server.models.book import Book

import logging

logger = logging.getLogger(__name__)

bp = Blueprint('books', __name__, url_prefix='/api')


# GET /api/books
@bp.get('/books')
def get_books():
	select_all = Book.query.all()
	books = [
		{
			'name': b.name,
			'author': b.author
		} for b in select_all
	]
	return jsonify({'books': books}), 200


# POST /api/books
@bp.post('/books')
def post_book():
	content_type = request.headers.get('Content-Type')
	if not content_type == 'application/json':
		return jsonify({'error': 'Invalid Content Type'}), 415

	request_params = request.json
	if not 'name' in request_params or not 'author' in request_params:
		return jsonify({'error': 'Bad Data'}), 400

	name = request_params['name']
	author = request_params['author']

	try:
		db.session.add(Book(name=name, author=author))
		db.session.commit()
		logger.info('Saved Book: %s saved successfully', name)
	except SQLAlchemyError:
		logger.error('Failed to save Book: %s to Database', name)
		return jsonify({'error': 'Database Error'}), 500

	return jsonify({'status': 'Created'}), 201
