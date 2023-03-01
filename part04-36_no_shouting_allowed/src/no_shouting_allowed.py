def no_shouting(list_of_strings: list) -> list:
    return [word for word in list_of_strings if not word.isupper()]
