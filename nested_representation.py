def rep_set(n):
    if n == 0:
        return []
    else:
        prev = rep_set(n - 1)
        return prev + [prev]

# Examples of operation
print(rep_set(0))  # Output: []
print(rep_set(1))  # Output: [[]]
print(rep_set(2))  # Output: [[], [[]]]
print(rep_set(3))  # Output: [[], [[]], [[], [[]]]]
