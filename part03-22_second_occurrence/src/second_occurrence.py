string = input()
subs = input()

index = string[string.find(subs) + len(subs) :].find(subs)

if index == -1:
    print("The substring does not occur twice in the string.")
else:
    print(
        f"The second occurrence of the substring is at index {index +  string.find(subs) + len(subs)}."
    )
