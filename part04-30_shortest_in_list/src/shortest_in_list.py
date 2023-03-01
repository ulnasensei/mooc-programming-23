def shortest(word_list: list) -> str:
    shortest_word = word_list[0]
    for i in range(1, len(word_list)):
        if len(word_list[i]) < len(shortest_word):
            shortest_word = word_list[i]
    return shortest_word
