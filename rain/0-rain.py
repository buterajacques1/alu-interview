#!/usr/bin/python3
def rain(walls):
    """Calculate how much rainwater is retained in a given list of walls.

    Args:
        walls (List[int]): A list of non-negative integers representing the
            heights of walls with unit width 1.

    Returns:
        int: The total amount of rainwater retained.

    """
    if not walls:
        return 0

    size = len(walls) - 1
    prev = walls[0]
    index = 0
    aux = 0
    water_retained = 0

    for i in range(1, size + 1):
        if walls[i] >= prev:
            aux = 0
            index = i
            prev = walls[i]
        else:
            aux += prev - walls[i]
            water_retained += prev - walls[i]

    if index < size:
        prev = walls[i]
        water_retained -= aux

        for i in range(size, index - 1, -1):
            if walls[i] >= prev:
                prev = walls[i]
            else:
                water_retained += prev - walls[i]

    return water_retained
