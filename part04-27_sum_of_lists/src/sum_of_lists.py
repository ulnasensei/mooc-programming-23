def list_sum(list_a: list, list_b: list) -> list:
    list_of_sums = []
    for i in range(len(list_a)):
        list_of_sums.append(list_a[i] + list_b[i])
    return list_of_sums
