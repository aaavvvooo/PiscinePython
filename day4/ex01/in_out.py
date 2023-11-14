def square(x: int | float) -> int | float:
    """
    This function calculates x ^ 2
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    This function calculates x ^ x
    """
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        """
        Closure part of the closer function
        """
        nonlocal count
        if (count == 0):
            count = x
        count = function(count)
        return (count)
    return inner


# Test part
# def main():
#     my_counter = outer(3, square)
#     print(my_counter())
#     print(my_counter())
#     print(my_counter())
#     print("---")
#     another_counter = outer(1.5, pow)
#     print(another_counter())
#     print(another_counter())
#     print(another_counter())


# if __name__ == "__main__":
#     main()
