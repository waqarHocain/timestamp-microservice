import unittest
import os

# local imports
from app import create_app


class TimestampTestCase(unittest.TestCase):
    """This class represents Timestamp microservice test case"""
    
    def setUp(self):
        """Define test variables"""
        self.app = create_app(config_name="development")
        self.client = self.app.test_client

    def test_it_returns_homepage_on_get_request(self):
        res = self.client().get("/")
        
        self.assertEqual(res.status_code, 200)
        self.assertIn(res.data, "Timestamp Microservice")


if __name__ == "__main__":
    unittest.main()
