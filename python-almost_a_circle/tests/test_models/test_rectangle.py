import unittest

from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from contextlib import redirect_stdout
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

    def test_area(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

        r = Rectangle(5, 7)
        self.assertEqual(r.area(), 35)


    def test_display(self):
        r1 = Rectangle(3, 2)
        expected_output = '###\n###\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

        r2 = Rectangle(2, 3)
        expected_output = '##\n##\n##\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r2.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)
