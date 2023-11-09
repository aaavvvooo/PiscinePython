from S1E9 import Character


class Baratheon(Character):
    """Class representing the Baratheon family. Inherits from Character."""
    def __init__(self, first_name, is_alive=True) -> None:
        """Constructor
Args:
first_name(str): first name of the character
is_alive(bool): True if the character is alive, False otherwise
        """
        super().__init__(first_name, is_alive)
        self.eyes = "brown"
        self.hair = "dark"
        self.family_name = "Baratheon"

    def __str__(self):
        """Return a string representation of the class"""
        return "<Bound method Baratheon.__str__ of"

    def __repr__(self):
        """Return a string representation of the class"""
        s = f"Vector: ('{self.family_name }', '{self.eyes}', '{self.hair}')"
        return s

    def die(self):
        """Boars are really dangerous"""
        self.is_alive = False


class Lannister(Character):
    """Class representing the Lannister family. Inherits from Character."""
    def __init__(self, first_name, is_alive=True) -> None:
        """Constructor"""
        super().__init__(first_name, is_alive)
        self.eyes = "blue"
        self.hair = "light"
        self.family_name = "Lannister"

    def __str__(self):
        """Return a string representation of the class"""
        return "<Bound method Lannister.__str__ of"

    def __repr__(self):
        """Return a string representation of the class"""
        s = f"Vector: ('{self.family_name }', '{self.eyes}', '{self.hair}')"
        return s

    def create_lannister(first_name, is_alive=True):
        """Only two Lannisters can create a Lannister"""
        return Lannister(first_name, is_alive)

    def die(self):
        """Watch out, a rock is falling."""
        self.is_alive = False
