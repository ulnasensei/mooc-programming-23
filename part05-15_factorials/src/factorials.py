def factorials(n: int) -> dict:
    d = {}
    for i in range(1, n + 1):
        factorial = 1
        for x in range(1, i + 1):
            factorial *= x
        d[i] = factorial

    return d
