import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue( is_triangle(1, 1, 1) )
        self.assertTrue( is_triangle(3, 4, 5) )
        self.assertTrue( is_triangle(3, 4, 6) )
        self.assertTrue( is_triangle(8, 10, 12) )
        self.assertTrue( is_triangle(100, 101, 200) )
        self.assertTrue( is_triangle(0.9, 1.0, 1.1) )

    def test_not_triangle(self):
        self.assertFalse( is_triangle(21, 10, 10) )
        self.assertFalse( is_triangle(2, 1, 1) )   # borderline case
        self.assertFalse( is_triangle(6, 10, 4) )  # borderline case
        self.assertFalse( is_triangle(6, 20, 4) )

    def test_invalid_argument_raises_exception(self):
        """any non-positive argument should raise ValueError"""
        with self.assertRaises(ValueError):
            b1 = is_triangle(-1, 2, 2)
            b2 = is_triangle( 1, 0, 2)

        with self.assertRaises(ValueError):
            b1 = is_triangle( 1, -1, 2)
            b2 = is_triangle( 1,  0, 2)

        with self.assertRaises(ValueError):
            b1 = is_triangle( 1, 2, -1)
            b2 = is_triangle( 1, 2,  0)

        with self.assertRaises(ValueError):
            b1 = is_triangle( -1, -1, -1)
            b2 = is_triangle( 0, 0, 0)
