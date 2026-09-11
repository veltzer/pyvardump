"""Behavioural tests for pyvardump's pure helpers."""

import unittest

from pyvardump import dump


class Sample:
    def __init__(self):
        self.a = 1
        self.b = "two"


class ObjectToMembersOrStringTests(unittest.TestCase):
    def test_object_with_dict_returns_vars(self):
        obj = Sample()
        self.assertEqual(dump.object_to_members_or_string(obj), {"a": 1, "b": "two"})

    def test_int_without_dict_returns_string(self):
        self.assertEqual(dump.object_to_members_or_string(5), "5")

    def test_string_without_dict_returns_string(self):
        self.assertEqual(dump.object_to_members_or_string("hello"), "hello")

    def test_none_returns_string(self):
        self.assertEqual(dump.object_to_members_or_string(None), "None")


class DefaultFuncTests(unittest.TestCase):
    def test_default_func_returns_dir_listing(self):
        result = dump.default_func(Sample())
        self.assertIn("a", result)
        self.assertIn("b", result)

    def test_default_func_on_int_returns_dir(self):
        # ints have a dir(), so the listing (not the type string) comes back
        self.assertIn("bit_length", dump.default_func(5))
