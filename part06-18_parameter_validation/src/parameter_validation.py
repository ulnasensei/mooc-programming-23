def new_person(name: str, age: int) -> tuple[str, int]:
    if type(name) != str or type(age) != int or len(name) == 0 or " " not in name or len(name) > 40 or age < 0 or age > 150:
        raise ValueError()
    return name, age
