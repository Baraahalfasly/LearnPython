def flipping_bits(n):
    # Flip the bits and ensure 32-bit result
    return ~n & 0xFFFFFFFF

# Test cases
print(flipping_bits(2147483647))  # ➞ 2147483648
print(flipping_bits(1))          # ➞ 4294967294
print(flipping_bits(4))          # ➞ 4294967291
