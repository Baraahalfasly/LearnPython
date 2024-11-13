def count_ones(num):
    return bin(num).count('1')

# Function test
print(count_ones(0))    # ➞ 0
print(count_ones(100))  # ➞ 3
print(count_ones(999))  # ➞ 8
