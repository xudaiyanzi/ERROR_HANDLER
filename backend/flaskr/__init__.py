from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy #, or_
from flask_cors import CORS
import random

from models import setup_db, Book

BOOKS_PER_SHELF = 8


def paginate_books(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * BOOKS_PER_SHELF
  end = start + BOOKS_PER_SHELF

  books = [book.format() for book in selection]
  current_books = books[start:end]

  return current_books

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  # CORS Headers 
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  
  @app.route('/books')
  def retrieve_books():
    selection = Book.query.order_by(Book.id).all()
    current_books = paginate_books(request, selection)

    if len(current_books) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'books': current_books,
      'total_books': len(Book.query.all())
    })

  @app.route('/books/<int:book_id>', methods=['PATCH'])
  def update_book(book_id):

    body = request.get_json()

    try:
      book = Book.query.filter(Book.id == book_id).one_or_none()
      if book is None:
        abort(404)

      if 'rating' in body:
        book.rating = int(body.get('rating'))

      book.update()

      return jsonify({
        'success': True,
        'id': book.id,
      })
      
    except:
      abort(400)

  @app.route('/books/<int:book_id>', methods=['DELETE'])
  def delete_book(book_id):
    try:
      book = Book.query.filter(Book.id == book_id).one_or_none()

      if book is None:
        abort(404)

      book.delete()
      selection = Book.query.order_by(Book.id).all()
      current_books = paginate_books(request, selection)

      return jsonify({
        'success': True,
        'deleted': book_id,
        'books': current_books,
        'total_books': len(Book.query.all())
      })

    except:
      abort(422)

  @app.route('/books', methods=['POST'])
  def create_book():
    body = request.get_json()

    new_title = body.get('title', None)
    new_author = body.get('author', None)
    new_rating = body.get('rating', None)

    ## hand the "search" here
    search = body.get('search', None)

    try:
      if search:
        selection = Book.query.filter(Book.title.ilike('%{}%'.format(search))).order_by(Book.id)
        current_books = paginate_books(request, selection)

        return jsonify({
        'success':True,
        'books':current_books,
        'total_books':len(selection.all())
        })
      
      else:
        book = Book(title=new_title, author=new_author, rating=new_rating)
        book.insert()

        selection = Book.query.order_by(Book.id).all()
        current_books = paginate_books(request, selection)

        return jsonify({
          'success': True,
          'created': book.id,
          'books': current_books,
          'total_books': len(Book.query.all())
        })

    except:
      abort(422)

  # @TODO: Create a new endpoint or update a previous endpoint to handle searching for a team in the title
  #        the body argument is called 'search' coming from the frontend. 
  #        If you use a different argument, make sure to update it in the frontend code. 
  #        The endpoint will need to return success value, a list of books for the search and the number of books with the search term
  #        Response body keys: 'success', 'books' and 'total_books'
  # @app.route("/books/search/<int:book_id>", methods=['GET'])
  # def search_book(book_id):
  #   try:
  #     book = Book.query.filter(Book.id == book_id).one_or_none()

  #     return jsonify({
  #       'success':True,
  #       'book':book.format()
  #     })

  #   except:
  #     abort(404)


  # @TODO: Review the above code for route handlers. 
  #        Pay special attention to the status codes used in the aborts since those are relevant for this task! 

  # @TODO: Write error handler decorators to handle AT LEAST status codes 400, 404, and 422. 
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'message':'bad request',
      'error': 400
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'sucess':False,
      'message':'not found',
      'error':404
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success':False,
      'message':'can not process the resource',
      'error':422
    }), 422

  @app.errorhandler(405)
  def not_allowed(error):
    return jsonify({
      'success':False,
      'message':'method is not allowed',
      'error':405
    }), 405

  # TEST: Practice writing curl requests. Write some requests that you know will error in expected ways.
  #       Make sure they are returning as expected. Do the same for other misformatted requests or requests missing data.
  #       If you find any error responses returning as HTML, write new error handlers for them. 

  return app

    