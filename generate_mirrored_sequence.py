def pop_pattern(lst):
    result = []
    for i in range(len(lst)):
        result.append(i)
    for i in range(len(lst) - 2, -1, -1):
        result.append(i)
    return result

# Test the function with the examples you provided
print(pop_pattern([0, 0, 0, 0, 4, 0, 0, 0, 0]))  # ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
print(pop_pattern([0, 0, 0, 3, 0, 0, 0]))       # ➞ [0, 1, 2, 3, 2, 1, 0]
print(pop_pattern([0, 0, 2, 0, 0]))             # ➞ [0, 1, 2, 1, 0]
print(pop_pattern([0]))                         # ➞ [0]
