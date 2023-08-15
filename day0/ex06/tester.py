from ft_filter import ft_filter


def isEven(nb) -> bool:
    if nb % 2 == 0:
        return True
    return False


def main():
    print(ft_filter.__doc__)
    mylist = [1, 2, 3, 4, 5]
    print(ft_filter(isEven, mylist))


if __name__ == "__main__":
    main()
