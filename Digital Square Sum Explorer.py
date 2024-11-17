def is_happy(n):
    seen = set()  # To track numbers we've already encountered to detect cycles
    while n != 1:
        if n in seen:
            return False  # If we see a number again, it means there's a cycle
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))  # Replace n with sum of squares of its digits
    return True  # If we reach 1, the number is happy

# Test cases
print(is_happy(67))    # ➞ False
print(is_happy(89))    # ➞ False
print(is_happy(139))   # ➞ True
print(is_happy(1327))  # ➞ False
print(is_happy(2871))  # ➞ False
print(is_happy(3970))  # ➞ True
