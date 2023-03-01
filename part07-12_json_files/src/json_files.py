import json


def print_persons(filename: str):
    with open(filename) as file:
        content = file.read()

    people = json.loads(content)

    for person in people:
        print(
            f'{person["name"]} {person["age"]} years ({", ".join(person["hobbies"])})'
        )
