def read_input(string: str, boundary_1: int, boundary_2: int) -> int:
    while True:
        try:
            number = int(input(string))
            assert boundary_1 < number < boundary_2
            return number
        except (ValueError, AssertionError):
            print(f"You must type in an integer between {boundary_1} and {boundary_2}")
