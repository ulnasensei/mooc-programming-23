def create_tuple(x: int, y: int, z: int) -> tuple:
    items = sorted((x, y, z))

    return (items[0], items[2], sum(items))
