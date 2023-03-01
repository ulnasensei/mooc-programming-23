string = input("Your input: ")

with open("wordlist.txt") as file:
    data = [x.strip() for x in file.readlines()]

output = []

for word in string.split():
    if word.lower() in data:
        output.append(word)
        continue
    output.append(f"*{word}*")

print(" ".join(output))
