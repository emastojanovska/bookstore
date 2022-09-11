from flask import Blueprint, jsonify, request
from models import db, Book

book_blueprint = Blueprint('book_api_routes', __name__, url_prefix='/api/book')


@book_blueprint.route('/all', methods=['GET'])
def get_all_books():
    all_books = Book.query.all()
    result = [book.serialize() for book in all_books]
    response = {"result" : result}
    return jsonify(response)


@book_blueprint.route('/create', methods=['POST'])
def create_book():
    try:
        book = Book()
        book.name = request.form["name"]
        book.slug = request.form["slug"]
        book.price = request.form["price"]
        book.image = request.form["image"]
        db.session.add(book)
        db.session.commit()
        response = {
            'message': 'Book is created successfully',
            'result': book.serialize()
        }
    except Exception as e:
        print(str(e))
        response = {
            'message': 'Book cannot be created',
        }
    return jsonify(response)


@book_blueprint.route('/<slug>', methods=['GET'])
def get_book_details(slug):
    book = Book.query.filter_by(slug=slug).first()
    if book:
        response = {'result': book.serialize()}
    else:
        response = {'message': 'No book found'}
    return jsonify(response)
