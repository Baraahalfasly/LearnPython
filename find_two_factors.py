def two_product(arr, target):
    seen = set()
    for num in arr:
        if num != 0 and target % num == 0:
            complement = target // num
            if complement in seen:
                return [complement, num]
        seen.add(num)
    return None

# Test cases
print(two_product([1, 2, -1, 4, 5], 20))  # ➞ [4, 5]
print(two_product([1, 2, 3, 4, 5], 10))  # ➞ [2, 5]
print(two_product([100, 12, 4, 1, 2], 15))  # ➞ None
