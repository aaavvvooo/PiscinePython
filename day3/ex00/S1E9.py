from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for a character in the Game of Thrones universe."""
    def __init__(self, first_name, is_alive=True) -> None:
        """Constructor
        Args:
        first_name(str): first name of the character
        is_alive(bool): True if the character is alive, False otherwise
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Kill the character"""
        pass


class Stark(Character):
    """Class representing the Stark family. Inherits from Character."""
    def __init__(self, first_name: str, is_alive: bool =True) -> None:
        """Constructor
Args:
first_name(str): first name of the character
is_alive(bool): True if the character is alive, False otherwise
        """
        self.family_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Wolder Frei entered the chat."""
        self.is_alive = False
