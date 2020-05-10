import os
import sys
import unittest
import requests
from unittest import TestCase


sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '.'))
import datetime_service as ds


class TestDatetimeAPI(TestCase):

    def test_datetime(self):
        '''
        Test for the data returned by get_datetime method. It compares the datatype
        '''
        datetimeObj = ds.get_datetime()
        self.assertIsInstance(datetimeObj, str)

    def test_test_api(self):

        data = requests.get("http://0.0.0.0:5000/message?name=irtiza")
        self.assertEqual(data.status_code, 200)


if __name__ == '__main__':
    unittest.main()
