import unittest

from functions.SublistFinder import SublistFinder


class TestSublistFinder(unittest.TestCase):

    def test_seq_check(self):
        sub = SublistFinder([1,3,3,1,2,3])
        self.assertTrue(sub.seq_check(), 'sublist found')

        sub = SublistFinder([1, 3, 3, 1, 2])
        self.assertFalse(sub.seq_check(), 'no sublist found')

if __name__ == '__main__':
    unittest.main()

