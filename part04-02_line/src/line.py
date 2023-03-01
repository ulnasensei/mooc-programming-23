def line(size, string):
    if len(string) == 0:
        print("*"*size)
    else:
        print(string[0]*size)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
