import unittest
import json
from flaskr import create_app
from models import setup_db

class ResourceTestCase(unittest.TestCase): # define a class for testing, use intuitive naming
    """"This class represents the __ test case"""
    
    def setUp(self): #setUp run before each test
        """Executed before each test. Define test variables and initialize app."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.database_name = 'test_db'
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)

        set_db(self.app, self.database_path)

    def tearDown(self): # teardow each test
        """Executed after each test"""
        pass

    def test_given_behavior(self): # test client request and evaluate response
        """Test ______________"""
        res = self.client().get('/') # save the response

        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()

