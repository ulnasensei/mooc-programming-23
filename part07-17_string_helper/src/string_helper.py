from string import ascii_letters, digits


def change_case(orig_string: str) -> str:
    return orig_string.swapcase()


def split_in_half(orig_string: str) -> tuple[str, str]:
    length = len(orig_string) // 2
    return orig_string[:length], orig_string[length:]


def remove_special_characters(orig_string: str) -> str:
    new = ""
    for letter in orig_string:
        if letter not in [*ascii_letters, *digits, " "]:
            continue
        new += letter

    return new
