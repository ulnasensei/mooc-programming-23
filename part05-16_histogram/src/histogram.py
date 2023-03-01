def histogram(string: str) -> None:
    stats = {}
    for letter in string:
        if letter not in stats:
            stats[letter] = 0
        stats[letter] += 1
    for key, value in stats.items():
        print(f"{key} {'*' * value}")
