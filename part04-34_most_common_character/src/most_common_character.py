def most_common_character(string: str) -> str:
    top_char = string[0]
    top_char_count = string.count(string[0])
    for letter in string:
        if letter  != top_char:
            count = string.count(letter)
            if count > top_char_count:
                top_char = letter
                top_char_count = count
    return top_char
