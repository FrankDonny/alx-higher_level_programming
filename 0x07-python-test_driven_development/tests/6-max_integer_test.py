import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    def test_max_integer(self):
        li = [12, 15, 4, 7, 10, 14]
        res = max_integer(li)
        self.assertEqual(res, 4)
