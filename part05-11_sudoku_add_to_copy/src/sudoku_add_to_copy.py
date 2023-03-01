def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    new_sudoku = [[] for row in sudoku]
    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            if row == row_no and col == column_no:
                new_sudoku[row].append(number)
            else:
                new_sudoku[row].append(0)

    return new_sudoku
