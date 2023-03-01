def distinct_numbers(numbers: list) -> list:
    numbers.sort()
    distinct = []

    for number in numbers:
        if number not in distinct:
            distinct.append(number)
    return distinct
