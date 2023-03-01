def generate_strong_password(length: int, include_number: bool, include_special: bool) -> str:
    from random import randint, choice, shuffle
    from string import ascii_lowercase, digits

    special_chars = "!?=+-()#"
    password = []

    # include both numbers and special characters
    if include_number and include_special:
        number_length = randint(1, length - 2)
        special_length = randint(1, length - number_length - 1)
        for i in range(length - number_length - special_length):
            password.append(choice(ascii_lowercase))
        for i in range(number_length):
            password.append(choice(digits))
        for i in range(special_length):
            password.append(choice(special_chars))
        shuffle(password)
        return "".join(password)

    # include numbers
    if include_number:
        number_length = randint(1, length - 1)
        for i in range(length - number_length):
            password.append(choice(ascii_lowercase))
        for i in range(number_length):
            password.append(choice(digits))
        shuffle(password)
        return "".join(password)

    # include special characters
    if include_special:
        special_length = randint(1, length - 1)
        for i in range(length - special_length):
            password.append(choice(ascii_lowercase))
        for i in range(special_length):
            password.append(choice(special_chars))
        shuffle(password)
        return "".join(password)

    # only letters
    for i in range(length):
        password.append(choice(ascii_lowercase))
    return "".join(password)


if __name__ == "__main__":
    for i in [5,6,8,12,14,16]:
        print(i)
        print(generate_strong_password(i, True, True))
