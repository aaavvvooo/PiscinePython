import sys
import string


def main(argv):
    try:
        assert len(argv) == 3, "the arguments are bad"
        length = int(argv[2])
        punct_list = list(map(lambda x: x in string.punctuation, argv[1]))
        if True in punct_list:
            raise AssertionError("the arguments are bad")
        print([elem for elem in argv[1].split(" ") if len(elem) > length])
    except Exception:
        print("Assertion error: the arguments are bad")


if __name__ == "__main__":
    main(sys.argv)
