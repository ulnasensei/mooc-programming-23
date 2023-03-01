def even_numbers(number_list: list) -> list:
    evens = []
    for number in number_list:
        if number % 2 == 0:
            evens.append(number)
    return evens
