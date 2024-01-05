#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print(f"{len(sys.argv) - 1} argument{'s' if len(sys.argv) > 2 else ''}: ", end="")
        print(*sys.argv[1:], sep=", ")
