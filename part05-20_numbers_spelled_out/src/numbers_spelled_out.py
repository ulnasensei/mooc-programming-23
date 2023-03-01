def dict_of_numbers() -> dict:
    numbers = {}
    for i in range(100):
        if i < 20:
            numbers[i] = parse_1_to_19(i)
        elif i % 10 == 0:
            print((i // 10) * 10)
            numbers[i] = parse_double_digit((i // 10) * 10)
        else:
            numbers[i] = parse_double_digit((i // 10) * 10) + "-" + parse_1_to_19(i % 10)
    return numbers


def parse_1_to_19(number: int) -> str:
    if number == 0:
        return "zero"
    if number == 1:
        return "one"
    if number == 2:
        return "two"
    if number == 3:
        return "three"
    if number == 4:
        return "four"
    if number == 5:
        return "five"
    if number == 6:
        return "six"
    if number == 7:
        return "seven"
    if number == 8:
        return "eight"
    if number == 9:
        return "nine"
    if number == 10:
        return "ten"
    if number == 11:
        return "eleven"
    if number == 12:
        return "twelve"
    if number == 13:
        return "thirteen"
    if number == 14:
        return "fourteen"
    if number == 15:
        return "fifteen"
    if number == 16:
        return "sixteen"
    if number == 17:
        return "seventeen"
    if number == 18:
        return "eighteen"
    if number == 19:
        return "nineteen"


def parse_double_digit(number: int) -> str:
    if number == 20:
        return "twenty"
    if number == 30:
        return "thirty"
    if number == 40:
        return "forty"
    if number == 50:
        return "fifty"
    if number == 60:
        return "sixty"
    if number == 70:
        return "seventy"
    if number == 80:
        return "eighty"
    if number == 90:
        return "ninety"
