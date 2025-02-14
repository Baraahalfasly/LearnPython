def count_elements(lst):
    count = 1  # Count the list itself
    for item in lst:
        if isinstance(item, list):
            count += count_elements(item)  # Recursively count sublists and elements
        else:
            count += 1  # Count non-list elements
    return count

def func(lst):
    return count_elements(lst) - 1  # Subtract 1 to exclude the outermost list

# Test cases
print(func([[], [], []]))  # ➞ 3
print(func([[3], [2], [1, 2]]))  # ➞ 7
print(func([]))  # ➞ 0
print(func([[[]]]))  # ➞ 2
