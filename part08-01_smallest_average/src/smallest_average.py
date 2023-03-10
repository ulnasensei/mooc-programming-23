def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    avg, smallest = sum(list(person1.values())[1:]) / 3, person1
    if sum(list(person2.values())[1:]) / 3 < avg:
        avg = sum(list(person2.values())[1:]) / 3
        smallest = person2
    elif sum(list(person3.values())[1:]) / 3 < avg:
        avg = sum(list(person3.values())[1:]) / 3
        smallest = person3

    return smallest
