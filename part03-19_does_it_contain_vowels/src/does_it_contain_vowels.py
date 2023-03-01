string = input()

for letter in ("a", "e", "o"):
    if letter in string:
        print(f"{letter} found")
    else:
        print(f"{letter} not found")

