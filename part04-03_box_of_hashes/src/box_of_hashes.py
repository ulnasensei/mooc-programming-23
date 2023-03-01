def line(size, string):
    if len(string) == 0:
        print("*"*size)
    else:
        print(string[0]*size)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    for i in range(0, height):
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
