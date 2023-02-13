import unittest

from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    def test_create_square(self):
        s = Square(5)
        self.assertEqual(s.id, 1)


if __name__ == '__main__':
    unittest.main()