import unittest
from backend import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), [0])

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    # After ensuring the above tests pass, the long ones only need to have their lengths checked
    def test_fibonacci_70(self):
        self.assertEqual(len(fibonacci(70)), 70)

    def test_fibonacci_1001(self):
        self.assertEqual(len(fibonacci(1001)), 1001)

    def test_fibonacci_negative(self):
        self.assertEqual(fibonacci(-1), [])

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), [])


if __name__ == '__main__':
    unittest.main()
