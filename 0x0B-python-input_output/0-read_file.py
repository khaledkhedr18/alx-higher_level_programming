""" Definition of the file reading function """


def read_file(filename=""):
    """ Prints the contents of the file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
