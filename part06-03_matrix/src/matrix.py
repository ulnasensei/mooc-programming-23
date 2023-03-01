def matrix_sum() -> int:
    items = []

    with open("matrix.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            items.extend([int(x) for x in line.split(",")])

    return sum(items)



def matrix_max() -> int:
    maximum = 0

    with open("matrix.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            for number in line.split(","):
                if int(number) > maximum:
                    maximum = int(number)
    return maximum


def row_sums() -> list:
    row_sum = []

    with open("matrix.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            row_sum.append(sum([int(x) for x in line.split(",")]))

    return row_sum
