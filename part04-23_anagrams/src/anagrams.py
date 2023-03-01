def anagrams(string_a: str, string_b: str) -> bool:
    return (sorted(string_a) == sorted(string_b))
