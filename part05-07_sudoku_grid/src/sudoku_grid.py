def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    block_status = [0 for i in range(10)]

    for row_index in range(row_no, row_no + 3):
        for col_index in range(column_no, column_no + 3):
            block_status[sudoku[row_index][col_index]] += 1
            print(block_status)

    for index in range(1, len(block_status)):
        if block_status[index] > 1:
            return False
    return True


def column_correct(sudoku: list, column_no: int) -> bool:
    col_status = [0 for i in range(10)]

    for row in sudoku:
        col_status[row[column_no]] += 1

    for index in range(1, len(col_status)):
        if col_status[index] > 1:
            return False
    return True


def row_correct(sudoku: list, row_no: int) -> bool:
    row_status = [0 for i in range(len(sudoku[row_no]) + 1)]

    for item in sudoku[row_no]:
        row_status[item] += 1

    for index in range(1, len(row_status)):
        if row_status[index] > 1:
            return False
    return True


def sudoku_grid_correct(sudoku: list) -> bool:
    for row_no in range(len(sudoku)):
        if not row_correct(sudoku, row_no):
            return False
    for col_no in range(len(sudoku[0])):
        if not column_correct(sudoku, col_no):
            return False
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not block_correct(sudoku, i, j):
                return False
    return True
