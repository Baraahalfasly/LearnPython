def ones_threes_nines(num):
    # Calculate the number of nines, threes, and ones
    nines = num // 9
    num %= 9
    threes = num // 3
    ones = num % 3
    
    # Format the output string
    return f"nines:{nines}, threes:{threes}, ones:{ones}"

# Test cases
print(ones_threes_nines(10))  # ➞ "nines:1, threes:0, ones:1"
print(ones_threes_nines(15))  # ➞ "nines:1, threes:2, ones:0"
print(ones_threes_nines(22))  # ➞ "nines:2, threes:1, ones:1"
