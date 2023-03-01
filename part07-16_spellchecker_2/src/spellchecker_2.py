from difflib import get_close_matches

string = input("Your input: ")

with open("wordlist.txt") as file:
    data = [x.strip() for x in file.readlines()]

output = []
suggestions = {}

for word in string.split():
    if word.lower() in data:
        output.append(word)
        continue
    output.append(f"*{word}*")
    suggestions[word] = get_close_matches(word, data)

print(" ".join(output))
print("suggestions:")
for key, value in suggestions.items():
    print(f'{key}: {", ".join(value)}')
