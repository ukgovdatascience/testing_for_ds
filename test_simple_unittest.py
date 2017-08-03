import unittest

from simple import mean


class TestSimple(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean(4, 5, 6), 4.5)  # wrong


if __name__ == '__main__':
    unittest.main()
