import unittest
import os

# local imports
from app import create_app
from app.main.utils import unixts_converter, date_analyzer


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


class TimestampTestCase(BaseTestCase):
    """Test suit for checking json response"""

    def test_it_handles_wrong_format_dates(self):
        res = self.client().get("/january%february%05") 
        res2 = self.client().get("/jflsurow398420")

        self.assertIn("none", res.data)
        self.assertIn("none", res2.data)

class UtilsTestCase(BaseTestCase):
    """Test suit for main.utils funcs"""
    def test_it_can_distinguish_unixts_and_date_str(self):
        unixts_1 = 1494246008
        unixts_2 = 0
        unixts_3 = 23879138

        date_str_1 = "jan 01 1970"
        date_str_2 = "may 2012"
        date_str_3 = "may be its not a date"

        self.assertEqual(date_analyzer(unixts_1), "unix_timestamp")
        self.assertEqual(date_analyzer(unixts_2), "unix_timestamp")
        self.assertEqual(date_analyzer(unixts_3), "unix_timestamp")

        self.assertEqual(date_analyzer(date_str_1), "natural_language")
        self.assertEqual(date_analyzer(date_str_2), "natural_language")
        self.assertEqual(date_analyzer(date_str_3), "natural_language")

    def test_it_returns_correct_date_for_unix_timestamp(self):
        unix_ts_1 = 1494246008
        expected_date_1 = "May 8, 2017"
        unix_ts_2 = 0
        expected_date_2 = "January 1, 1970"

        self.assertEqual(expected_date_1, unixts_converter(unix_ts_1))
        self.assertEqual(expected_date_2, unixts_converter(unix_ts_2))



if __name__ == "__main__":
    unittest.main()
