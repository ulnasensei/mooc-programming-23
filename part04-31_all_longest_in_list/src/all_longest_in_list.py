def all_the_longest(word_list: list) -> list:
    longest_word_length = 0
    for word in word_list:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return [word for word in word_list if len(word) == longest_word_length]
