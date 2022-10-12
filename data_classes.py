# represent data structure
# define data structure
import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass()#frozen = True)
class Person:
    name: str
    address: str
    active: bool = True  # default values
    email_addresses: list[str] = field(default_factory=list) # default list
    id: str = field(init = False, default_factory=generate_id)  # random generated ID, can not be initialised by a user

    _search_string: str = field(init=False, repr=False)  # dont show the search string

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"

    # def __init__(self, name: str, address: str):
    #     self.name = name
    #     self.address = address
    # allow strings to be shown for the class
    # def __str__(self) -> str:
    #     return f"{self.name}, {self.address}"

def main() -> None:
    person = Person(name = "John", address = "123 Main St.")
    # person.name = "pop"
    print(person)
    

if __name__ == "__main__":
    main()