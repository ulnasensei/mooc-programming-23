layers = int(input("Layers: "))

size = (2 * layers) - 1

matrix = [[(x, y) for y in range(size)] for x in range(size)]


for row in matrix:
    print(row)
