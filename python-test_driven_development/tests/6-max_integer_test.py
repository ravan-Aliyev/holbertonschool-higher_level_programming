#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_at_end(self):
        result = max_integer([3, 5, 6, 7])
        self.assertEqual(result, 7)

    def test_at_beggining(self):
        result = max_integer([7, 5, 6, 3])
        self.assertEqual(result, 7)

    def test_at_middle(self):
        result = max_integer([5, 4, 7, 6, 3])
        self.assertEqual(result, 7)

    def test_negative(self):
        result = max_integer([5, 4, 7, -6, 3])
        self.assertEqual(result, 7)

    def test_all_negative(self):
        result = max_integer([-5, -4, -7, -6, -3])
        self.assertEqual(result, -3)

    def test_one_input(self):
        result = max_integer([5])
        self.assertEqual(result, 5)
