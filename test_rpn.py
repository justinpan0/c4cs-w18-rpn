import unittest
import rpn


class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate("1 2 -")
        self.assertEqual(-1, result)

    def test_mul(self):
        result = rpn.calculate("4 2 *")
        self.assertEqual(8, result)

    def test_div(self):
        result = rpn.calculate("6 2 /")
        self.assertEqual(3, result)

    def test_exp(self):
        result = rpn.calculate("6 2 ^")
        self.assertEqual(36, result)
