import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):

    valid_triangles = [
            (1, 1, 1),
            (3, 4, 5),
            (3, 4, 6),  
            ]

    def test_valid_triangle(self):
        for a,b,c in self.valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertTrue( is_triangle(a, b, c), msg)

    not_valid_triangles = [
            (21, 10, 10),
            (2, 1, 1),
            (6, 10, 4),
            (6, 20, 4),
            ( 1, 2, 4) 
            ]
    def test_not_triangle(self):
        for a,b,c in self.not_valid_triangles:
            with self.subTest():
                self.assertFalse( is_triangle(a, b, c))

    def test_invalid_argument_raises_exception(self):
        """any non-positive argument should raise ValueError"""
        with self.assertRaises(ValueError):
            b1 = is_triangle(-1, 2, 2)

        with self.assertRaises(ValueError):
            b1 = is_triangle( 1, -1, 2)

        with self.assertRaises(ValueError):
            b1 = is_triangle( 1, 2, -1)

        with self.assertRaises(ValueError):
            b1 = is_triangle( -1, -1, -1)
        