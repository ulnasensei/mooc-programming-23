def spruce_line(width, max_width):
    space_count = (max_width - width) // 2
    print(" " * space_count + "*" * width + " " * space_count)

def spruce(height: int):
    print("a spruce!")
    max_width = (2 * height) - 1
    for i in range(1, height + 1):
        width = (2 * i) - 1
        spruce_line(width, max_width)
    spruce_line(1, max_width)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
