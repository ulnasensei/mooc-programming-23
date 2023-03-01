def who_won(game_board: list) -> int:
    player_one = 0
    player_two = 0
    for row in game_board:
        for piece in row:
            if piece == 1:
                player_one += 1
            elif piece == 2:
                player_two += 1
    if player_one > player_two:
        return 1
    if player_two > player_one:
        return 2
    return 0
