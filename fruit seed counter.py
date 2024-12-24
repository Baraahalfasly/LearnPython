def total_seeds(fruit):
    # Calculate the number of seeds based on the number of letters in the fruit name
    return len(fruit) * 2 + 5

# Test cases
print(total_seeds("watermelon"))  # ➞ 25
