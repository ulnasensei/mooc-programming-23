number = int(input())

if number % 2 == 0:
    for i in range(1, (number // 2) + 1):
        print(i)
        print(number - (i - 1))
else:
    for i in range(1, (number // 2) + 2):
        print(i)
        print(number - (i - 1)) if i != (number // 2) + 1 else None
