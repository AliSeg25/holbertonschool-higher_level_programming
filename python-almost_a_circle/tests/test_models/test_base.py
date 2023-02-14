import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import os
import json

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


    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            json_content = file.read()
            expected_content = json.dumps([r1.to_dictionary(), r2.to_dictionary()])
            self.assertEqual(json_content, expected_content)

        os.remove("Rectangle.json")
    
    def test_from_json_string(self):
        # Test avec une liste de dictionnaires non vide
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

if __name__ == '__main__':
    unittest.main()