def blocks(n):
    # Formula: b(n) = 0.5 * n^2 + 5.5 * n - 1
    return int(0.5 * n**2 + 5.5 * n - 1)

# Test cases
print(blocks(1))  # Output: 5
print(blocks(2))  # Output: 12
print(blocks(5))  # Output: 39
