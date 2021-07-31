import unittest
import json
from flaskr import create_app
from models import set_db

class ResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.database_name = 'test_db'
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)

        set_db(self.app, self.database_path)

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_given_behavior(self):
        """Test ______________"""
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()

