def parse_recipes(filename: str) -> dict:
    data = []
    recipes = {}
    space = True
    with open(filename) as file:
        lines = [x.strip() for x in file.readlines()]

    for line in lines:
        if space:
            data.append([line])
            space = False
            continue
        if len(line) == 0:
            space = True
            continue
        data[-1].append(line)
    for recipe in data:
        recipes[recipe[0]] = {"prep_time": int(recipe[1]), "ingredients": recipe[2:]}
    return recipes


def search_by_name(filename: str, word: str) -> list:
    recipes = parse_recipes(filename)
    result = []

    for name in recipes.keys():
        if word.lower() in name.lower():
            result.append(name)
    return result


def search_by_time(filename: str, prep_time: int) -> list:
    recipes = parse_recipes(filename)
    result = []

    for recipe_name, details in zip(recipes.keys(), recipes.values()):
        if details.get("prep_time") <= prep_time:
            result.append(
                f"{recipe_name}, preparation time {details.get('prep_time')} min"
            )
    return result


def search_by_ingredient(filename: str, ingredient: str) -> list:
    recipes = parse_recipes(filename)
    result = []

    for recipe_name, details in zip(recipes.keys(), recipes.values()):
        if ingredient in details.get("ingredients"):
            result.append(
                f"{recipe_name}, preparation time {details.get('prep_time')} min"
            )
    return result
