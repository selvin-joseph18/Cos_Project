from src.code import calculate_cos
import unittest

class Cos_Test(unittest.TestCase):
    def test_positive_angle_values(self):
        self.assertEqual(0.15425144988758405, calculate_cos.calculate_cos(30))

    def test_negative_angle_values(self):
        self.assertEqual(-0.7596879128588213, calculate_cos.calculate_cos(-15))

    def test_type_exception(self):
        self.assertRaises(TypeError, calculate_cos.calculate_cos('angle'))
