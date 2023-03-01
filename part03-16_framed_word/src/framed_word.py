string = input()

length = len(string)

start = (30 - length) // 2

print("*" * 30)
print(f"*{' ' * (start if length % 2 == 1 else start -1 )}{string}{' ' * (start - 1)}*")
print("*" * 30)
