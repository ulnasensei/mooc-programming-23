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
