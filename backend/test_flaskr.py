import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book

class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('student', 'student','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }

        # # binds the app to the current context
        # with self.app.app_context():
        #     self.db = SQLAlchemy()
        #     self.db.init_app(self.app)
        #     # create all tables
        #     self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
#        You can feel free to write additional tests for nuanced functionality,
#        Such as adding a book without a rating, etc. 
#        Since there are four routes currently, you should have at least eight tests. 
    ### I need to add data to the table first
    ### to do this, I use the command line below

    ## $psql -f books.psql -U student -d bookshelf_test

    # def test_pagination(self):
    #     """Test the pagination"""
    #     res = self.client().get('/books')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     ### be careful!!!! self.assertTrue VS self.assertEqual
    #     self.assertTrue(data['total_books'])
    #     self.assertTrue(len(data['books']))

    def test_search_book(self):
        # searched by title
        res = self.client().post('/books', json={'search': 'Novel'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['books']))
        self.assertTrue(data['total_books'])

    ## it is not a 404 error
    def test_search_book_not_found(self):
        res = self.client().post('/books', json={'search': 'haha'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['books']),0)
        self.assertEqual(data['total_books'],0)


    # def test_update_a_book_rating(self):
    #     """Test API can get a single book (GET request)."""
    #     res = self.client().patch('/books/3', json={'rating': 1})
    #     data = json.loads(res.data)
    #     book = Book.query.filter(Book.id == 3).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['id'], 3)
    #     self.assertEqual(book.format()['rating'], 1)


    # # def test_post_book(self):
    # #     """Test API can post a book (POST request)."""
    # #     res = self.client().post('/books', json=self.new_book)
    # #     data = json.loads(res.data)

    # #     self.assertEqual(res.status_code, 200)
    # #     self.assertEqual(data['success'], True)
    # #     self.assertTrue(data['created'])
    # #     self.assertTrue(len(data['books']))
    # #     self.assertTrue(data['total_books'])


    # # def test_delete_book(self):
    # #     """Test API can delete a book (DELETE request)."""
    # #     res = self.client().delete('/books/24')
    # #     book = Book.query.filter(Book.id == 24).one_or_none()
    # #     data = json.loads(res.data)

    # #     self.assertEqual(res.status_code, 200)
    # #     self.assertEqual(data['success'], True)
    # #     self.assertEqual(data['deleted'],24)
    # #     self.assertEqual(book, None)
    # #     self.assertTrue(data['total_books'])
    # #     self.assertTrue(len(data['books']))

    # def test_error_404_get_book_not_found(self):
    #     """Test API can get a single book (GET request)."""
    #     res = self.client().get('/books?page=10')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['sucess'], False)
    #     self.assertEqual(data['message'], 'not found')

    # def test_error_405_method_not_allowed(self):
    #     res = self.client().post('/books/4')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'method is not allowed')

    # def test_error_422_not_processable(self):
    #     res = self.client().delete('/books/100')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'can not process the resource')

    # def test_error_400_bad_request(self):
    #     res = self.client().patch('/books/10')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'bad request')

# Optional: Update the book information in setUp to make the test database your own! 


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()