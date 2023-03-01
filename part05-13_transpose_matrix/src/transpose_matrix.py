def transpose(matrix: list):
    size = len(matrix)
    for x in range(size):
        for y in range(x + 1, size):
            matrix[y][x], matrix[x][y] = (matrix[x][y], matrix[y][x])
