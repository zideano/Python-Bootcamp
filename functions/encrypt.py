import string


class Encrypt:

    @staticmethod
    def encrypt(text, shift):
        """
        INPUT: text as a string and an integer for the shift value.
        OUTPUT: The shifted text after being run through the Caeser cipher.
        """

        plain = string.ascii_lowercase
        cipher = [] * len(plain)
        plaintext = text.lower()
        cipher_text = [] * len(text)

        """
        Encrypt the plain text by performing the modulo operation 
        on the alphabet, then map a character to the encrypted char    
        """
        for i, x in enumerate(plain):
            cipher.insert((i + shift) % 26, x)

        for j, x in enumerate(plaintext):
            for k, v in enumerate(plain):
                if x == v:
                    cipher_text.insert(j, cipher[k])
                    break
                elif x == ' ':
                    cipher_text.insert(j, ' ')
                    break

        return ''.join(cipher_text)
