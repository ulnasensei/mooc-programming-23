def greatest_number(a, b, c) ->int:
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
