#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""

    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([101]), 101)

    def test_identical(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_max_start(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([8, 1, 12, 14, 16, 2, 30]), 30)

    def test_unordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 4, 2]), 4)

    def test_unordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([23, 333, 222, 333, 1024, 11, 33, 66, 44, 55]), 1024)

    def test_positives_and_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([-1024, 89, 98, 1080, -256, -512]), 1080)
