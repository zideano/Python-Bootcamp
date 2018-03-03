class StringManipulation:

    def replace_and_switch(self, name):
        """
        Substitute a vowel with the char 'x'
        and invert first and last letter of the
        string.
        :param name: Input string
        :return: final string
        """
        def __init__(self):
            self.string = ''

        vowel = ['a', 'e', 'i', 'o', 'u']

        try:
            lowercase_string = str(name.lower())
            result = [] * len(name)
            found = False

        except Exception as e:
            print('Input has to be a string: {}'.format(e))

        for i, v in enumerate(lowercase_string):
            for j in vowel:
                if v == j:
                    result.insert(i, 'x')
                    found = True
                    break
            if found:
                found = False
                continue
            else:
                result.insert(i, v)

        first = result[0]
        last = result[-1]

        result[0] = last
        result[-1] = first.upper()

        return ''.join(result)
