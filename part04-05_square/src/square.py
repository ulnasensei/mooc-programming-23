def line(size, string):
    if len(string) == 0:
        print("*" * size)
    else:
        print(string[0] * size)


def square(size, character):
    # You should call function line here with proper parameters
    for i in range(0, size):
        line(size, character)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
