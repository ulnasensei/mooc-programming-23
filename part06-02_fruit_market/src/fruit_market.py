def read_fruits() -> dict:
    fruits = {}

    with open('fruits.csv', 'r') as fruit_file:
        for line in fruit_file:
            line = line.replace("\n", "")
            fruit = line.split(";")[0]
            price = float(line.split(";")[1])
            fruits[fruit] = price

    return fruits
