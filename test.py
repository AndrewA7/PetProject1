import unittest

from triangle_area import triangle_area


class MyTestCase(unittest.TestCase):
    def test_zero_side(self):
        assert triangle_area(4, 4, 0) == "side can't be 0"

    def test_wrong_side(self):
        assert triangle_area(2, 3, 34) == "Incorrect triangle"

    def test_int_values(self):
        assert triangle_area(4, 6, 9) == 9.562

    def test_float_values(self):
        assert triangle_area(4.9, 6.1, 3.8) == 9.305