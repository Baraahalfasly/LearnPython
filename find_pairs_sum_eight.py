def sums_up(lst):
    result = []
    seen = set()
    
    for num in lst:
        complement = 8 - num
        if complement in seen:
            result.append([complement, num])
        seen.add(num)
    
    return {"pairs": result}

# Test cases
print(sums_up([1, 2, 3, 4, 5]))  # {"pairs": [[3, 5]]}
print(sums_up([1, 2, 3, 7, 9]))  # {"pairs": [[1, 7]]}
print(sums_up([10, 9, 7, 2, 8]))  # {"pairs": []}
print(sums_up([1, 6, 5, 4, 8, 2, 3, 7]))  # {"pairs": [[2, 6], [3, 5], [1, 7]]}
