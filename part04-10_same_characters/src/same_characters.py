def same_chars(string, a, b):
    last_index = len(string) - 1
    if a > last_index or b > last_index:
        return False
    if string[a] == string[b]:
        return True
    return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
