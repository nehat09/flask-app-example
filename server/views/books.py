
from flask import Blueprint

bp = Blueprint('books', __name__, url_prefix='/api')

# GET /api/book
@bp.get("/books")
def get_books():
	return {"books": []}
