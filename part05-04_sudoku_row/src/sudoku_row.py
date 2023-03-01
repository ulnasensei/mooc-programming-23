def row_correct(sudoku: list, row_no: int) -> bool:
    row_status = [0 for i in range(len(sudoku[row_no]) + 1)]

    for item in sudoku[row_no]:
        row_status[item] += 1

    for index in range(1, len(row_status)):
        if row_status[index] > 1:
            return False
    return True
