def line(size, string):
    if len(string) == 0:
        print("*" * size)
    else:
        print(string[0] * size)


def triangle(size):
    # You should call function line here with proper parameters
    for i in range(1, size + 1):
        line(i, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
