#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import doctest

if __name__ == "__main__":
    doctest.testfile("../simple_pypi_template/simple_pypi_template.py")
    doctest.testfile("../simple_pypi_template/submodule.py")
