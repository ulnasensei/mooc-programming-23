def separate_characters(my_string: str) -> tuple[str, str, str]:
    from string import ascii_letters, punctuation

    letters = ""
    punct = ""
    special_chars = ""

    for letter in my_string:
        if letter in ascii_letters:
            letters += letter
        elif letter in punctuation:
            punct += letter
        else:
            special_chars += letter

    return letters, punct, special_chars
