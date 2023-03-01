def sum_of_positives(integer_list: list) -> int:
    result = 0
    for number in integer_list:
        if number >= 0:
            result += number
    return result
