import unittest
from shapes.circle import Circle
from shapes.triangle import Triangle
from factory import create_shape
from area_calculator import calculate_area
from math import pi

class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), pi * 4, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_factory_circle(self):
        shape = create_shape("circle", 3)
        self.assertAlmostEqual(calculate_area(shape), pi * 9)

    def test_factory_triangle(self):
        shape = create_shape("triangle", 3, 4, 5)
        self.assertAlmostEqual(calculate_area(shape), 6.0)

if __name__ == "__main__":
    unittest.main()
