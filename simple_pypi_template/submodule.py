#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__test__ = {'import_test': """
                           >>> from simple_pypi_template.submodule import *

                           """}


def func_of_submodule(args, kwargs="..."):
    """
    Function description

    Example/s of use (and excutable test/s via doctest):
    >>> func_of_submodule("...")

    :param args: arg description.
    :param kwargs: arg description. By default: "..."
    :return:
    """

    # My function content ...


def func_create_file(path_to_file):
    """
    Function description

    Example/s of use (and excutable test/s via doctest):
    >>> func_create_file("file.txt")
    'line in file'

    :param path_to_file: set a path to file
    :return: string with first line in file
    """

    with open(path_to_file, "w") as f:
        f.write("line in file")

    with open(path_to_file, "r") as f:
        return f.readline()


__test__ = {
    'clean_test_files': """
                        >>> from pathlib import Path
                        >>> Path("file.txt").unlink()

                        """}
