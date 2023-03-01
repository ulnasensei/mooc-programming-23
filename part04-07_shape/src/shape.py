def line(size, string):
    if len(string) == 0:
        print("*" * size)
    else:
        print(string[0] * size)


def shape(width: int, triangle_character: str, heigth: int, rectangle_character: str):
    for i in range(1, width + 1):
        line(i, triangle_character)
    for i in range(0, heigth):
        line(width, rectangle_character)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
