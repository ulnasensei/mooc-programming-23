def column_correct(sudoku: list, column_no: int) -> bool:
    col_status = [0 for i in range(10)]

    for row in sudoku:
        col_status[row[column_no]] += 1

    for index in range(1, len(col_status)):
        if col_status[index] > 1:
            return False
    return True
