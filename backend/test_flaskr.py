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

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
#        You can feel free to write additional tests for nuanced functionality,
#        Such as adding a book without a rating, etc. 
#        Since there are four routes currently, you should have at least eight tests. 
    def test_get_books(self):
        """Test API can get a book (GET request)."""
        res = self.client().get('/books')
        self.assertEqual(res.status_code, 200)

    def test_get_a_book(self):
        """Test API can get a single book (GET request)."""
        res = self.client().get('/books/2')
        self.assertEqual(res.status_code, 200)

    def test_get_book_not_found(self):
        """Test API can get a single book (GET request)."""
        res = self.client().get('/books/0')
        self.assertEqual(res.status_code, 404)

    def test_post_book(self):
        """Test API can post a book (POST request)."""
        res = self.client().post('/books', data=self.new_book)
        self.assertEqual(res.status_code, 201)


    def test_delete_book(self):
        """Test API can delete a book (DELETE request)."""
        res = self.client().delete('/books/2')
        self.assertEqual(res.status_code, 200)

    def test_delete_book_not_found(self):
        """Test API can delete a book (DELETE request)."""
        res = self.client().delete('/books/0')
        self.assertEqual(res.status_code, 404)

# Optional: Update the book information in setUp to make the test database your own! 


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()