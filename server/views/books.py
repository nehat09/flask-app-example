from flask import Blueprint
from flask import request, jsonify

from server import db
from server.models.book import Book

bp = Blueprint('books', __name__, url_prefix='/api')

# GET /api/book
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
	request_params = request.json
	if not 'name' in request_params or not 'author' in request_params:
		return jsonify({'error': 'Bad Data'}), 400

	name = request_params['name']
	author = request_params['author']

	db.session.add(Book(name=name, author=author))
	db.session.commit()

	return jsonify({'status': 'Created'}), 201
