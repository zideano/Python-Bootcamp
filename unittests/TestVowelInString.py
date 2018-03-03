import unittest

from functions.findVowels import StringManipulation


class TestVowelInString(unittest.TestCase):

    def test_vowel_in_string_then_invert_first_last_char(self):
        string = 'James'
        string_manipulation = StringManipulation()
        result = string_manipulation.replace_and_switch(string)

        self.assertEqual(result, 'sxmxJ')
        self.assertEqual(len(result), len(string))

        string2 = 'Alfred'
        result2 = string_manipulation.replace_and_switch(string2)
        self.assertNotEquals(result2, 'Alfred')
        self.assertTrue(result2, 'dlfrxX')

if __name__ == '__main__':
    unittest.main()