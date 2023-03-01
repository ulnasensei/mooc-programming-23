def chessboard(size):
    for row in range(0, size):
        line = ""
        if row % 2 == 0:
            for col in range(0, size):
                if col % 2 == 0:
                    line += "1"
                else:
                    line += "0"
        else:
            for col in range(0, size):
                if col % 2 == 0:
                    line += "0"
                else:
                    line += "1"
        print(line)

# Testing the function
if __name__ == "__main__":
    chessboard(3)
