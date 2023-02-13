import unittest

from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
from io import StringIO
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
        
    def test_init(self):
        s = Square(5, 2, 3, 4)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)
        
    def test_str(self):
        s = Square(5)
        self.assertEqual(str(s), "[Square] ({}) 0/0 - 5".format(s.id))
        
    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)
        
    def test_display(self):
        s = Square(2)
        expected_output = "##\n##\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            self.assertEqual(buf.getvalue(), expected_output)
            
    def test_update(self):
        s = Square(1)
        s.update(2, 3, 4, 5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)
        
    def test_to_dictionary(self):
        s = Square(2, 1, 2, 3)
        expected_dict = {'id': 3, 'size': 2, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_dict)
        
if __name__ == '__main__':
    unittest.main()
