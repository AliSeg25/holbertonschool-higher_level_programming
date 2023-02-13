import unittest

from models.rectangle import Rectangle
from models.base import Base
#import models.rectangle
#import models.base


#Base = __import__('models.base').Base
#Rectancle = __import__('models.rectangle').Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_width_positive_integer(self):
        r = Rectangle(10, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_width_not_integer(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.width = "not an integer"

    def test_width_not_positive(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -5
        
if __name__ == '__main__':
    unittest.main()
