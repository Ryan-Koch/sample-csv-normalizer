#import things
import unittest

from normalizer import Normalizer

class TestConversionMethods(unittest.TestCase):
    norm = Normalizer()


    def test_timezone_converstion(self):
        norm = Normalizer()
        test_timestamp = "10/2/04 8:44:11 AM"
        expected_value = "2004-10-02T12:37:11-04:00"

        test_value = norm.timezone_convert_to_est(test_timestamp)
        self.assertEqual(expected_value, test_value)

    def test_convert_to_float_seconds(self):
        norm = Normalizer()
        test_timestamp = "100:1:0.0"
        expected_result = (100*3600) + (60*1) + (0)

        test_value = norm.convert_to_float_seconds(test_timestamp)
        self.assertEqual(expected_result, test_value)

    def test_zip_code_validation(self):
        norm = Normalizer()
        test_zip_4_len = '1234'
        test_zip_3_len = '023'
        test_zip_1_len = '1'
        test_zip_5_len = '12345'

        test_4_len = norm.zip_code_validation(test_zip_4_len)
        self.assertEqual(test_4_len, '01234')

        test_3_len = norm.zip_code_validation(test_zip_3_len)
        self.assertEqual(test_3_len, '00023')

        test_1_len = norm.zip_code_validation(test_zip_1_len)
        self.assertEqual(test_1_len, '00001')

        test_5_len = norm.zip_code_validation(test_zip_5_len)
        self.assertEqual(test_5_len, '12345')

    