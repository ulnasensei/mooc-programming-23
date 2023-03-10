def row_sums(my_matrix: list) -> list:
    i = 0
    limit = len(my_matrix)
    while i < limit:
        my_matrix[i].append(sum(my_matrix[i]))
        i += 1
