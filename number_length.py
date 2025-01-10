def digits_count(number):
    # Convert number to string and calculate its length
    return len(str(number))

# Test cases
print(digits_count(4666))               # Output: 4
print(digits_count(544))                # Output: 3
print(digits_count(121317))             # Output: 6
print(digits_count(0))                  # Output: 1
print(digits_count(12345))              # Output: 5
print(digits_count(1289396387328))      # Output: 13
