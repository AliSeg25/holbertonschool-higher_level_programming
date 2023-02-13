import unittest
import models.rectangle
from models.base import Base
"""a"""


class TestBase(unittest.TestCase):
    def test_id(self):
        # Test création d'objets avec ID spécifié
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

        b2 = Base(200)
        self.assertEqual(b2.id, 200)

        # Test création d'objets sans ID spécifié
        b3 = Base()
        self.assertEqual(b3.id, 1)

        b4 = Base()
        self.assertEqual(b4.id, 2)

        b5 = Base()
        self.assertEqual(b5.id, 3)

        

if __name__ == '__main__':
    unittest.main()