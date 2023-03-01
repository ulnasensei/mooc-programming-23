def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    from random import randint

    lottery = []
    for i in range(amount):
        while True:
            x = randint(lower, upper)
            if x in lottery:
                continue
            lottery.append(x)
            break
    return sorted(lottery)
