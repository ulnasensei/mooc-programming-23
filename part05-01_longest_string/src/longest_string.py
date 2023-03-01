def longest(strings: list) -> str:
    longest_word = ""
    for word in strings:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
