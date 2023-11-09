class calculator():
    """A simple calculator class for vectors"""
    def __init__(self, vector: list) -> None:
        """Constructor"""
        self.vct = vector

    def __add__(self, object):
        """Addition operator overloaded
        Adds a vallue to each element of the vector"""
        self.vct = [self.vct[i] + object for i in range(len(self.vct))]
        print(self.vct)
        return self

    def __mul__(self, object):
        """Multiplication operator overloaded
        Multiplies each element of the vector by a value"""
        self.vct = [self.vct[i] * object for i in range(len(self.vct))]
        print(self.vct)
        return self

    def __sub__(self, object):
        """Subtraction operator overloaded
        Subtracts a value from each element of the vector"""
        self.vct = [self.vct[i] - object for i in range(len(self.vct))]
        print(self.vct)
        return self

    def __truediv__(self, object):
        """Division operator overloaded
        Divides each element of the vector by a value"""
        try:
            if object == 0:
                raise ZeroDivisionError
            self.vct = [self.vct[i] / object for i in range(len(self.vct))]
            print(self.vct)
            return self
        except ZeroDivisionError:
            print("Division by zero is undefined")
            return self
