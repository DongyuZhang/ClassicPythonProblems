import unittest

from fibonacci import fib4

class TestFibonacci(unittest.TestCase):
    def testValue(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 1)
        self.assertEqual(fib4(2), 1)
        self.assertEqual(fib4(3), 2)
        self.assertEqual(fib4(4), 3)
        self.assertEqual(fib4(5), 5)

if __name__ == "__main__":
    unittest.main()