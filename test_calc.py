"""
CLI:

W/O if __name__ == '__main__'

    python -m unittest test_calc.py

With if __name__ == '__main__'
    python test_calc.py

"""
# test_calc.py is a naming convention we should follow!


# Python standard library
import unittest

# 👀 ONLY import with module name here if it's in the SAME directory
import calc


class TestCalc(unittest.TestCase):
    """4 .... docts -> there are 4 test completed"""

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # Using the 'context manager' -> call our function normally
        with self.assertRaises(ValueError):  # 👍 recommended
            calc.divide(10, 0)

        # self.assertRaises(ValueError, calc.divide, 10, 0)  # 👎 depcrecated


# 👍 Better run test directly within our editor
# 🧠 __name__ == '__main__'

if __name__ == '__main__':
    unittest.main()
