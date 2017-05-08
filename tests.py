import unittest
import os

# local imports
from app import create_app


class BaseTestCase(unittest.TestCase):
    """This class represents the base test case from which other
    classes will inherit"""
    
    def setUp(self):
        """Define test variables"""
        self.app = create_app(config_name="development")
        self.client = self.app.test_client


class HomepageTestCase(BaseTestCase):
    """Test suite for homepage"""

    def test_it_returns_homepage_on_get_request(self):
        res = self.client().get("/")
        
        self.assertEqual(res.status_code, 200)
        self.assertIn("Timestamp Microservice", res.data)

    def test_there_is_an_input_box(self):
        res = self.client().get("/")
        input_html = '<input class="time_input" type="text">'

        self.assertIn(input_html, res.data)


if __name__ == "__main__":
    unittest.main()
