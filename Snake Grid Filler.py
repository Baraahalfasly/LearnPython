def snakefill(n):
    # Calculate the total number of cells in the grid
    total_cells = n * n
    # Start with 1 filled cell
    filled_cells = 1
    # Count the number of steps
    steps = 0

    # Keep doubling the filled cells until they exceed the total cells
    while filled_cells <= total_cells:
        steps += 1
        filled_cells *= 2  # Double the filled cells in each step

    return steps - 1  # Subtract 1 because the last step exceeds the grid

# Examples
print(snakefill(3))  # ➞ 3
print(snakefill(6))  # ➞ 5
print(snakefill(24))  # ➞ 9
