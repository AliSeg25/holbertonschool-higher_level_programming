import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

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

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_str = Base.to_json_string([dictionary])
        self.assertEqual(type(json_str), str)

        empty_json_str = Base.to_json_string([])
        self.assertEqual(empty_json_str, "[]")

        none_json_str = Base.to_json_string(None)
        self.assertEqual(none_json_str, "[]")

        

if __name__ == '__main__':
    unittest.main()