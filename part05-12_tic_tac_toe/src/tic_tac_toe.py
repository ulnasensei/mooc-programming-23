def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    if x > 2 or x < 0 or y > 2 or y < 0:
        return False
    if game_board[y][x] != "":
        return False
    game_board[y][x] = piece
    return True
