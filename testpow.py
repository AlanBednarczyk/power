import unittest
import power


class TestPow(unittest.TestCase):

    def test_pow(self):
        result = power.pow(10, 5)
        self.assertEqual(result, 100000)

    def test_pow2(self):
        result = 2 ** 3
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()