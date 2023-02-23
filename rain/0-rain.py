#!/usr/bin/python3
def rain(walls):
    """Calculate how many square units of water will be retained after it rains.

    Args:
        walls (List[int]): A list of non-negative integers representing the
            heights of walls with unit width 1.

    Returns:
        int: The total amount of rainwater retained.

    """
    if not walls:
        return 0

    n = len(walls)
    left = [0] * n
    right = [0] * n

    # Calculate the maximum height of walls to the left of each position.
    left[0] = walls[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], walls[i])

    # Calculate the maximum height of walls to the right of each position.
    right[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], walls[i])

    # Calculate the amount of water retained at each position.
    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - walls[i]

    return water
