#!/usr/bin/python3
""" Defines a function that writes into a file"""


def write_file(filename="", text=""):
    """ A function that writes into a file
    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write into the file.
    Returns:
        The number of bytes written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
