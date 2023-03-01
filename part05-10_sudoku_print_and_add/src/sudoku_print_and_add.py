def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number


def print_sudoku(sudoku: list):
    for row_no in range(len(sudoku)):
        if row_no % 3 == 0 and row_no != 0:
            print()
        for col_no in range(len(sudoku[row_no])):
            if col_no % 3 == 0 and col_no != 0:
                print(" ", end="")
            cell = sudoku[row_no][col_no]
            print(cell if cell != 0 else "_", end=" ")
        print()
