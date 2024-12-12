def flip_list(lst):
    # Check if the input list is empty
    if not lst:
        return []
    
    # Determine the orientation and flip
    if isinstance(lst[0], list):
        # If the first element is a list, flatten the list
        return [item[0] for item in lst]
    else:
        # If the first element is not a list, create a vertical list
        return [[item] for item in lst]

# Test cases
print(flip_list([1, 2, 3, 4]))  # ➞ [[1], [2], [3], [4]]
print(flip_list([[5], [6], [9]]))  # ➞ [5, 6, 9]
print(flip_list([]))  # ➞ []
