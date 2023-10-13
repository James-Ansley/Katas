import unittest

from karate_chop import chop


class TestStringMethods(unittest.TestCase):
    def test_chop(self):
        self.assertEqual(-1, chop(3, []))
        self.assertEqual(-1, chop(3, [1]))
        self.assertEqual(0, chop(1, [1]))

        self.assertEqual(0, chop(1, [1, 3, 5]))
        self.assertEqual(1, chop(3, [1, 3, 5]))
        self.assertEqual(2, chop(5, [1, 3, 5]))
        self.assertEqual(-1, chop(0, [1, 3, 5]))
        self.assertEqual(-1, chop(2, [1, 3, 5]))
        self.assertEqual(-1, chop(4, [1, 3, 5]))
        self.assertEqual(-1, chop(6, [1, 3, 5]))

        self.assertEqual(0, chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(8, [1, 3, 5, 7]))


if __name__ == '__main__':
    unittest.main()
