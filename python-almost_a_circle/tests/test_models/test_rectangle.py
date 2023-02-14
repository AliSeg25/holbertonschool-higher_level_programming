import unittest

from models.rectangle import Rectangle
from models.base import Base

from io import StringIO
from contextlib import redirect_stdout


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

    def test_str(self):
            r = Rectangle(14, 16, 12, 15, 25)
            self.assertEqual(str(r), "[Rectangle] (25) 12/15 - 14/16")

        
    def test_update(self):
            r = Rectangle(1, 2, 3, 4, 5)
            r.update(10, 20, 30, 40, 50)
            self.assertEqual(r.id, 10)
            self.assertEqual(r.width, 20)
            self.assertEqual(r.height, 30)
            self.assertEqual(r.x, 40)
            self.assertEqual(r.y, 50)

    def test_load_from_file(self):

        file_path = "Rectangle.json"
        if os.path.exists(file_path):
            os.remove(file_path)

        res = Rectangle.load_from_file()

        self.assertEqual(res, [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertIsInstance(list_rectangles_output, list)
        self.assertNotEqual(list_rectangles_output, [])

        self.assertEqual(len(list_rectangles_output), len(list_rectangles_input))

        for rect1, rect2 in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(rect1, rect2)

        os.remove(file_path)
