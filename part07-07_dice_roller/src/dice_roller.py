from random import choice


def roll(die: str) -> int:
    dies = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]}

    return choice(dies[die])


def play(die1: str, die2: str, times: int) -> tuple[int, int, int]:
    die1_won = 0
    die2_won = 0
    tie = 0

    for i in range(times):
        d1 = roll(die1)
        d2 = roll(die2)

        if d1 > d2:
            die1_won += 1
        elif d2 > d1:
            die2_won += 1
        else:
            tie += 1

    return die1_won, die2_won, tie
