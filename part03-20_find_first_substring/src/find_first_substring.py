string = input()
char = input()

index = string.find(char)

if index + 3 <= len(string):
    print(string[index: index + 3])
