#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} {}:".format(argc, "argument" if argc == 1 else "arguments"))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
