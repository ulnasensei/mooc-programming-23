def squared(word, size):
    times = ((size ** 2) // len(word)) + 1
    string = word * times
    for i in range(0, size ** 2, size):
        print(string[i: i + size])
