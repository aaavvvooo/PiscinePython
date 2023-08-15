import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        exit(1)
    else:
        if sys.argv[1].isdigit() or sys.argv[1][1:].isdigit() and\
                    sys.argv[1][0] == "-":
            if int(sys.argv[1]) % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        else:
            raise AssertionError("argument is not an integer")

except Exception as error:
    print(type(error).__name__ + ": " + str(error))
