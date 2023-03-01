def palindromes(string: str) -> bool:
    return string == string[::-1]

while True:
    string = input()
    if palindromes(string):
        print(f"{string} is a palindrome!")
        break
    print("that wasn't a palindrome")
