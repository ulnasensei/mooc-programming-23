# from string import ascii_uppercase


# layers = int(input("Layers: "))

# size = (2 * layers) - 1
# center = size // 2
# print(size, center)

# matrix = [[(x, y) for y in range(size)] for x in range(size)]
# matrix_letter = [[" " for y in range(size)] for x in range(size)]

# for row in matrix:
#     print(row)

# for i in range(layers + 1):
#     if i == 0:
#         matrix_letter[center][center] = ascii_uppercase[i]
#         continue
#     for j in range(i, center + 1):
#         for k in range(j, center + 1):
#             matrix_letter[center - j][center - k] = ascii_uppercase[i]
#             matrix_letter[center - j][center + k] = ascii_uppercase[i]
#             # matrix_letter[center - j][center] = ascii_uppercase[i]
#             # matrix_letter[center + j][center] = ascii_uppercase[i]
#             # matrix_letter[center][center - k] = ascii_uppercase[i]
#             # matrix_letter[center][center + k] = ascii_uppercase[i]
#             # matrix_letter[center - j][center + j] = ascii_uppercase[i]
#             # matrix_letter[center + j][center - j] = ascii_uppercase[i]


# for row in matrix_letter:
#         print("".join(row))


from string import ascii_uppercase

result = []

# Get your number of layers
N = int(input("Give a number between 2 and 26: "))
assert 2<=N<=26, 'Wrong number'

for i in range(N):
    # update existing rows
    for j, string in enumerate(result):
        result[j] = ascii_uppercase[i] + string + ascii_uppercase[i]
        print(ascii_uppercase[i] + string + ascii_uppercase[i])

    # add top and bottom row
    result.append((2*i+1)*ascii_uppercase[i])
    if i != 0:
        result.insert(0, (2*i+1)*ascii_uppercase[i])

# print result
for line in result:
    print(line)
