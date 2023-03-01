def oldest_person(people: list) -> str:
    oldest = people[0][0]
    oldest_age = people[0][1]

    for person in people:
        if person[1] < oldest_age:
            oldest_age = person[1]
            oldest = person[0]

    return oldest
