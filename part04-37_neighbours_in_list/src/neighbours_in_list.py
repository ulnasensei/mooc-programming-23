def longest_series_of_neighbours(numbers: list) -> int:
    longest_final = 1
    longest = 1
    for i in range(1, len(numbers)):

        if abs(numbers[i] - numbers[i - 1]) == 1:
            longest += 1
        else:
            longest = 1
        longest_final = max(longest_final, longest)

    return longest_final
