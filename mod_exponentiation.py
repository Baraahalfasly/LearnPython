def mod(base, exp, k):
    return pow(base, 2**exp, k)

# Test cases
print(mod(10, 1, 99))   # ➞ 1
print(mod(3, 2, 15))    # ➞ 6
print(mod(123, 20, 1234)) # ➞ 391
