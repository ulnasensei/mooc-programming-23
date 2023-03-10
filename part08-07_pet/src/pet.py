class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int) -> None:
        self.name: str = name
        self.species: str = species
        self.year_of_birth: int = year_of_birth


def new_pet(name: str, species: str, year_of_birth: int) -> Pet:
    return Pet(name, species, year_of_birth)
