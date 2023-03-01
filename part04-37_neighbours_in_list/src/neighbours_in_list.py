def longest_series_of_neighbours(numbers: list) -> int:
    longest_final = 0
    longest = 1
    for i in range(len(numbers) - 1):

        if (numbers[i] + 1 == numbers[i + 1]) or (numbers[i] - 1 == numbers[i + 1]):
            longest += 1
            print(longest)
            if longest > longest_final:
                longest_final = longest
        else:
            if longest > longest_final:
                longest_final = longest
                longest = 1

    return longest_final

# I need to reset the counter somewhere, but I have no idea.
