import unittest
from roman_num_translator.src.roman_num_translator import roman_to_int, WrongOrderException


class TestRomanNumbers(unittest.TestCase):

    def test_roman_to_int_happycase(self):

        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('II'), 2)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('XCIX'), 99)

    def test_roman_to_int_wrong_order(self):

        with self.assertRaises(WrongOrderException):
            roman_to_int('IIV')

        
            roman_to_int('XD')

