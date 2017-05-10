import unittest
import os

# local imports
from app import create_app
from app.main.utils import (
        unixts_converter,
        date_analyzer,
        date_converter,
        date_to_timestamp
    )


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
        res = self.client().get("/january%20february%2005") 
        res2 = self.client().get("/jflsurow398420")

        self.assertIn("null", res.data)
        self.assertIn("null", res2.data)

    def test_it_handles_correct_format_dates(self):
        res = self.client().get("/1970%201%20jun")
        res2 = self.client().get("/mar%2011%202068")
        res3 = self.client().get("/14%20aug%201947")
        
        expected_res = "June 1, 1970"
        expected_res2 = "March 11, 2068"
        expected_res3 = "August 14, 1947"

        self.assertIn(expected_res, res.data)
        self.assertIn(expected_res2, res2.data)
        self.assertIn(expected_res3, res3.data)

    def test_it_handles_unix_timestamps_correctly(self):
        res = self.client().get("/1494315371")
        res2 = self.client().get("/0")
        res3 = self.client().get("/44444444")

        expected_res = "May 9, 2017"
        expected_res2 = "January 1, 1970"
        expected_res3 = "May 30, 1971"

        self.assertIn(expected_res, res.data)
        self.assertIn(expected_res2, res2.data)
        self.assertIn(expected_res3, res3.data)

    def test_date_is_present_in_unixtimestamp_and_natural_language_form(self):
        res = self.client().get("/jan 20 2016")

        res_date = "January 20, 2016"
        res_timestamp = "1453248000"

        self.assertIn(res_date, res.data)
        self.assertIn(res_timestamp, res.data)


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

    def test_it_returns_correct_date_for_a_date_str(self):
        date_str_1 = "jan 01 1970"
        date_str_2 = "05 may 2012"
        date_str_3 = "1970 01 jun"

        date_str_4 = "auggg 14 2012"
        date_str_5 = "not so good day"
        date_str_6 = "okay!"

        self.assertEqual(date_converter(date_str_1), "January 1, 1970")
        self.assertEqual(date_converter(date_str_2), "May 5, 2012")
        self.assertEqual(date_converter(date_str_3), "June 1, 1970")

        self.assertEqual(date_converter(date_str_4), None)
        self.assertEqual(date_converter(date_str_5), None)
        self.assertEqual(date_converter(date_str_6), None)

    def test_it_returns_correct_timestamp_for_a_date_str(self):
        self.assertEqual(date_to_timestamp("jan 20 2016"), 1453248000)
        self.assertEqual(date_to_timestamp("11 mar 1977"), 226886400)
        self.assertEqual(date_to_timestamp("2120 11 march"), 4739558400)


if __name__ == "__main__":
    unittest.main()
