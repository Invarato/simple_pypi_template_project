#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..pypi_template.pypi_template import func_of_my_module
from ..pypi_template.submodule import func_of_submodule, func_create_file


class TestPypiTemplate(unittest.TestCase):

    def setUp(self):
        # Define setup code (clean in tearDown)
        pass

    def tearDown(self):
        # Define tear down code (init in setUp)
        pass

    def test_func_of_my_module(self):
        returned = func_of_my_module(123, "hello", kwarg_b="Something good")

        self.assertEqual(returned, "Something good to return", "My error message: Returned value is bad")


class TestSubmodule(unittest.TestCase):

    def setUp(self):
        self.test_path = "my_test_file.txt"

    def tearDown(self):
        from pathlib import Path
        try:
            Path(self.test_path).unlink()
        except FileNotFoundError:
            pass
        self.test_path = None

    def test_func_of_submodule(self):
        func_of_submodule("Example of data")

    def test_func_create_file(self):
        returned = func_create_file(self.test_path)

        self.assertEqual(returned, "line in file", "My error message: File did not pass test")


if __name__ == '__main__':
    unittest.main()
