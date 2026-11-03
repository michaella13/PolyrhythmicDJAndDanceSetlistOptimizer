import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()