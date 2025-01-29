def find_glasses(items):
    for i, item in enumerate(items):
        if 'O' in item and '-' in item:
            return i
        elif item == "O-O" or item == "O##O":
            return i
    return -1

# Test cases
print(find_glasses(["phone", "O-O", "coins", "keys"]))  # Should print: 1
print(find_glasses(["OO", "wallet", "O##O", "O----O"]))  # Should print: 3
print(find_glasses(["O--#--O", "dustO---Odust", "more dust"]))  # Should print: 1
print(find_glasses(["glasses", "sun", "pool"]))  # Should print: -1
