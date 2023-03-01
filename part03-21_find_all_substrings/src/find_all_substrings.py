string = input()
char = input()

while True:
    if len(string) < 3:
        break
    index = string.find(char)
    if index + 3 <= len(string) and index != -1:
        print(string[index:index + 3])
        string = string[index + 1:]
    else:
        break
