from random import sample
def words(n: int, beginning: str) -> list:
    with open("words.txt") as file:
        lines = [x.strip() for x in file.readlines()]
    valid_words = list(filter(lambda x: x.startswith(beginning), lines))
    if len(valid_words) < n:
        raise ValueError()

    return sample(valid_words, n)
