while True:
    number = int(input())
    if number <= 0:
        print("Thanks and bye!")
        break
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of the number {number} is {factorial}")
