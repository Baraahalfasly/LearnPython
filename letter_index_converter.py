def title_to_number(column_title):
    result = 0
    for char in column_title:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

# Test cases
print(title_to_number("A"))  # 1
print(title_to_number("R"))  # 18
print(title_to_number("AB")) # 28
