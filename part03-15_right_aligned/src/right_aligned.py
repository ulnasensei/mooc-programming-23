string = input()

length = len(string)

if length < 20:
    print("*" * (20 - length) + string)
else:
    print(string)
