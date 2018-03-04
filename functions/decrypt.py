import string


class Decrypt:

    @staticmethod
    def decrypt(text, shift):
        """
        INPUT: A shifted message and the integer shift value
        OUTPUT: The plain text original message.
        """

        plain = string.ascii_lowercase
        cipher = [] * len(plain)
        cipher_text = text.lower()
        plaintext = [] * len(text)

        """
        Decrypt the cipher text by performing the opposite 
        modulo operation     
        """
        for i, x in enumerate(plain):
            cipher.insert((i - shift) % 26, x)

        for j, x in enumerate(cipher_text):
            for k, v in enumerate(plain):
                if x == v:
                    plaintext.insert(j, cipher[k])
                    break
                elif x == ' ':
                    plaintext.insert(j, ' ')
                    break

        return ''.join(plaintext)
