import sys
import string


def letter_counter(line: str) -> dict:
    """Counts the number of each type of character in a given string."""
    d = dict()
    d["upper letters"] = 0
    d["lower letters"] = 0
    d["punctuation marks"] = 0
    d["spaces"] = 0
    d["digits"] = 0
    for letter in line:
        if letter.isupper():
            d["upper letters"] += 1
        elif letter.islower():
            d["lower letters"] += 1
        elif letter.isspace():
            d["spaces"] += 1
        elif letter.isdigit():
            d["digits"] += 1
        elif letter in string.punctuation or letter == "\n":
            d["punctuation marks"] += 1
    return d


def main(argv):
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if len(argv) == 1:
            line = input("What is the text to count?\n")
        else:
            line = argv[1]
        d = letter_counter(line)
        print(f"The string contains {len(line)} characters:")
        for elem in d:
            print(f"{d[elem]} {elem}")
    except Exception as error:
        print(type(error).__name__ + ": " + str(error))


if __name__ == "__main__":
    main(sys.argv)
