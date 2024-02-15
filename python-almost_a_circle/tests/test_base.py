import json
import os
import unittest

from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        """This method is called before each test"""

        Base._Base__nb_objects = 0
        self.base = Base()

    def test_init(self): 
        """Test the __init__ method"""

        self.assertEqual(self.base.id, 1)

    def test_id_passed(self):
        """Test if the Base class is correctly saving the ID passed to it"""

        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_to_json_string(self):
        """Test the to_json_string method"""

        self.assertEqual(self.base.to_json_string([{'key': 'value'}]), '[{"key": "value"}]')
        self.assertEqual(self.base.to_json_string(None), '[]')

    def test_from_json_string(self):
        """Test the from_json_string method"""

        self.assertEqual(self.base.from_json_string('[{"key": "value"}]'), [{'key': 'value'}])
        self.assertEqual(self.base.from_json_string(None), [])

    def test_save_to_file(self):
        """Test the save_to_file method"""
        
        if hasattr(self.base, 'to_dictionary'):
            self.base.id = 123
            Base.save_to_file([self.base])
            with open("Base.json", "r") as file:
                self.assertEqual([self.base.to_dictionary()], json.load(file))

    def test_create(self):
        """Test the create method"""
        
        if hasattr(self.base, 'update'):
            base1 = self.base.create(id=345)
            self.assertEqual(base1.id, 345)

    def test_load_from_file(self):
        """Test the load_from_file method"""
        
        if hasattr(self.base, 'to_dictionary'):
            self.base.id = 123
            Base.save_to_file([self.base])
            list_of_bases = Base.load_from_file()
            self.assertEqual(list_of_bases[0].id, 123)

    def tearDown(self):
        """This method is called after each test"""

        try:
            os.remove("Base.json")
        except:
            pass


if __name__ == '__main__':
    unittest.main()