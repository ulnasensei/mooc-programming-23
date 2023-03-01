def find_words(search_term: str) -> list:
    result = []

    with open("words.txt") as file:
        words = [x.strip() for x in file.readlines()]

    if "*" in search_term:
        if search_term[0] == "*":
            for word in words:
                if word.endswith(search_term[1:]):
                    result.append(word)
            return result
        if search_term[-1] == "*":
            for word in words:
                if word.startswith(search_term[:-1]):
                    result.append(word)
            return result
    if "." in search_term:
        length = len(search_term)
        for word in words:
            if len(word) != length:
                continue
            match_status = True
            for search_letter, word_letter in zip(search_term, word):
                if search_letter == ".":
                    continue
                if search_letter != word_letter:
                    match_status = False
                    break
            if match_status:
                result.append(word)


    for word in words:
        if search_term == word:
            result.append(word)
    return result
