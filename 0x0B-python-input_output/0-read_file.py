def read_file(filename=""):
    with open(filename, "r") as f:
        print(f.read(), end="")
