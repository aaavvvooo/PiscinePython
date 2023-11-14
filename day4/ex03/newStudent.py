import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates random id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class for student
    """
    name: str
    surname: str
    login: str = field(init=False)
    active: bool = True
    id: str = field(init=False)

    def __init__(self, name, surname):
        """
        Constructor.
        """
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError("Name and surname must be strings")
        self.name = name
        self.surname = surname
        self.login = (name[0] + surname).lower()
        self.id = generate_id()


# try:
#     student = Student(name = "Edward", surname = "agle")
#     print(student)
#     student = Student(name = "Edward", surname = 1)
#     print(student)
# except Exception as e:
#     print(e)
