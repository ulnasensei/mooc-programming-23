number = int(input())

for i in range(1, number + 1, 2):
    print(i + 1) if i + 1 <= number else None
    print(i)
