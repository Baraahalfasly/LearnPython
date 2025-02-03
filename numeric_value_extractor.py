def num_split(num):
    if num == 0:
        return [0]
    
    abs_num = abs(num)
    sign = -1 if num < 0 else 1
    digits = []
    
    while abs_num > 0:
        digits.insert(0, sign * (abs_num % 10))
        abs_num //= 10
    
    for i in range(len(digits)):
        digits[i] *= 10 ** (len(digits) - i - 1)
    
    return digits

# Test examples
print(num_split(39))    # [30, 9]
print(num_split(-434))  # [-400, -30, -4]
print(num_split(100))   # [100, 0, 0]
