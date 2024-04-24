#!/usr/bin/python3
""" Definition of the file reading function """


def read_file(filename=""):
    """ Prints the contents of the file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
