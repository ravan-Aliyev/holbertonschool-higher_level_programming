import io
import json
import os
from re import S
import unittest
from contextlib import redirect_stdout

from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(5, 10, 15, 25)
        self.test_cases = [
            {"params": (1,), "expected": (1, 0, 0)},
            {"params": (1, 2), "expected": (1, 2, 0)},
            {"params": (1, 2, 3), "expected": (1, 2, 3)},
        ]

    def test_attributes(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 10)
        self.assertEqual(self.square.y, 15)
        self.assertEqual(self.square.id, 25)

    def test_area(self):
        self.assertEqual(self.square.area(), 25)

    def test_to_dictionary(self):
        expected = {"x": 10, "y": 15, "id": 25, "size": 5}
        self.assertEqual(self.square.to_dictionary(), expected)

    def test_update(self):
        self.square.update(30, 35, 40, 45)
        self.assertEqual(self.square.size, 35)
        self.assertEqual(self.square.x, 40)
        self.assertEqual(self.square.y, 45)
        self.assertEqual(self.square.id, 30)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            self.square.size = "invalid"

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            self.square.x = "invalid"

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            self.square.y = "invalid"

    def test_Square_initialization(self):
        for test_case in self.test_cases:
            square = Square(*test_case["params"])
            self.assertEqual((square.size, square.x, square.y), test_case["expected"])

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_str(self):
        self.assertEqual(str(self.square), "[Square] (25) 10/15 - 5")

    def test_display_without_x_y(self):
        self.square.x = 0
        self.square.y = 0
        expected_output = "\n".join(["#"*5 for _ in range(5)]) + "\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.square.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display_without_y(self):
        self.square.x = 10
        self.square.y = 0
        expected_output = "\n".join([" "*10 + "#"*5 for _ in range(5)]) + "\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.square.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display(self):
        expected_output = "\n"*15 + "\n".join([" "*10 + "#"*5 for _ in range(5)]) + "\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.square.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_create(self):
        square_dict = {'id': 89, 'size': 10, 'x': 2, 'y': 3}
        square = Square.create(**square_dict)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", mode="r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file(self):
        square = Square(1)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            content = json.load(file)
            self.assertEqual(content, [square.to_dictionary()])

    def test_load_from_file_no_file(self):
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_load_from_file(self):
        square = Square(1, 2, 3, 5)
        Square.save_to_file([square])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0].to_dictionary(), square.to_dictionary())

    def tearDown(self):
        """This method is called after each test"""

        try:
            os.remove("Square.json")
        except:
            pass


if __name__ == '__main__':
    unittest.main()