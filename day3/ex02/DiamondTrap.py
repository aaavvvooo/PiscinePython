from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing the King. Inherits from Baratheon and Lannister."""
    def __init__(self, first_name: str, is_alive=True) -> None:
        """Constructor"""
        Baratheon.__init__(self, first_name, is_alive)
        
    @property
    def hairs(self):
        print("barev")
        return self.hair


    def set_eyes(self, eyes: str) -> None:
        """Set the eyes color of the King"""
        self.eyes = eyes

    @hairs.setter
    def hairs(self, hair: str) -> None:
        """Set the hair color of the King"""
        self._hair = hair

    def get_eyes(self) -> str:
        """Return the eyes color of the King"""
        return self.eyes

    def get_hairs(self) -> str:
        """Return the hair color of the King"""
        return self.hair
