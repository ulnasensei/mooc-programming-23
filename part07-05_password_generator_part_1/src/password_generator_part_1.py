def generate_password(length: int) -> str:
    from random import choice
    from string import ascii_lowercase

    password = ""

    for i in range(length):
        password += choice(ascii_lowercase)

    return password
