def is_disarium(n):
    # Convert the number to a string to extract its digits
    digits = str(n)
    
    # Calculate the sum of each digit raised to its position (starting from 1)
    total = sum(int(digit) ** (i + 1) for i, digit in enumerate(digits))
    
    # Check if the total equals the original number
    return total == n

# Test examples
print(is_disarium(75))   # False
print(is_disarium(135))  # True
print(is_disarium(544))  # False
print(is_disarium(518))  # True
print(is_disarium(466))  # False
print(is_disarium(8))    # True
