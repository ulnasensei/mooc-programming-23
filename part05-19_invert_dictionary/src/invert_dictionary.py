def invert(dictionary: dict):
    keys = [key for key in dictionary.keys()]
    key_value_pairs = [x for x in dictionary.items()]
    for key, value in key_value_pairs:
        dictionary[value] = key
    for key in keys:
        del dictionary[key]
