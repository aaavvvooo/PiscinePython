from typing import Any, List


def calculate_mean(args: List[float]):
    """
    Helper function, that calculates the mean.
    Mean equals sum of all elements divided by the number of elements.
    """
    if len(args) == 0:
        print("ERROR")
        return None
    print(f"mean: {str(sum(args) / len(args))}")


def calculate_median(args: List[float]):
    """
    Helper function that calculates the median.
    """
    if len(args) == 0:
        print("ERROR")
        return None
    args.sort()
    if len(args) % 2 == 1:
        print(f"median: {args[len(args) // 2]}")
    else:
        median = (args[len(args) // 2] + args[(len(args) // 2) - 1]) / 2
        print(f"median: {median}")


def calculate_quartile(args: List[float]):
    """
    Helper function, that calculates Q1 and Q3.
    """
    if len(args) == 0:
        print("ERROR")
        return None
    quarts = []
    args.sort()
    quarts.append(args[int(len(args) / 4)])
    quarts.append(args[int(3 * len(args) / 4)])
    print(f"quartile: {quarts}")


def calculate_std(args: List[int]):
    """
    Helper function that calculates standard deviation.
    """
    if len(args) == 0:
        print("ERROR")
        return None
    mean = sum(args) / len(args)
    summa = 0
    for elem in args:
        summa += (elem - mean) ** 2
    std = (summa / len(args)) ** 0.5
    print(f"std is : {std}")


def calculate_var(args: List[int]):
    """
    Helper function, that calculates varience.
    """
    if len(args) == 0:
        print("ERROR")
        return None
    mean = sum(args) / len(args)
    summa = 0
    for elem in args:
        summa += (elem - mean) ** 2
    std = (summa / len(args)) ** 0.5
    print(f"std is : {std ** 2}")


def ft_statistics(*args: Any, **kwargs: Any):
    """
    Function takes dataset from args, and in kwargs takes the statistic
    parameters, that should be calculated  on that dataset.
    """
    vals = kwargs.values()
    for elem in vals:
        if elem == "mean":
            calculate_mean(list(args))
        elif elem == "median":
            calculate_median(list(args))
        elif elem == "quartile":
            calculate_quartile(list(args))
        elif elem == "std":
            calculate_std(list(args))
        elif elem == "var":
            calculate_var(list(args))


# Test part

# def main():
#     ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
#     print("-----")
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
#     print("-----")
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
#     print("-----")
#     ft_statistics(toto="mean", tutu="median", tata="quartile")

# if __name__ == "__main__":
#     main()