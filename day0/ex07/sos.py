import sys
import string


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '/'}


def main(argv):
    try:
        arr = []
        assert len(argv) == 2, "the arguments are bad"
        for _ in argv[1]:
            if _.upper() not in MORSE_CODE_DICT.keys() or\
                    _ in string.punctuation:
                raise Exception()
            else:
                arr.append(MORSE_CODE_DICT[_.upper()])
        print(" ".join(arr))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == '__main__':
    main(sys.argv)
