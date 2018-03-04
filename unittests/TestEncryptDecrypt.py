import unittest

from functions.decrypt import Decrypt
from functions.encrypt import Encrypt


class TestEncryptDecrypt(unittest.TestCase):

    def test_encrypt_function(self):
        text = 'Get this message to the main server'
        expected = 'trg guvf zrffntr gb gur znva freire'
        shift = 13

        result = Encrypt.encrypt(text, shift)
        self.assertTrue(result, expected)
        self.assertNotEqual(result, 'wrong text')
        self.assertEqual(result, expected)


    def test_decrypt_function(self):
        text = 'trg guvf zrffntr gb gur znva freire'
        expected = 'Get this message to the main server'
        shift = 13

        result = Decrypt.decrypt(text, shift)
        self.assertTrue(result, expected)
        self.assertNotEqual(result, 'wng dggf')
        self.assertEqual(result, expected)
        self.assertFalse(result, 'rhdhj dhh')


if __name__ == '__main__':
    unittest.main()
