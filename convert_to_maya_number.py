def maya_number(n):
    maya_symbols = {
        0: " ",
        1: "o",
        2: "o o",
        3: "o o o",
        4: "o o o o",
        5: "-",
        6: "- o",
        7: "- o o",
        8: "- o o o",
        9: "- o o o o"
    }
    
    # Convert the number to a string to easily process each digit
    digits = str(n)
    
    result = []
    
    for i, digit in enumerate(digits):
        digit = int(digit)
        
        # For the first place (the shell), use "@"
        if i == 0:
            result.append("@")
        
        # Add the Maya representation for the current digit
        result.append(maya_symbols[digit])
    
    return result

# Test cases
print(maya_number(39))     # ➞ ["o", "o o o o - - -"]
print(maya_number(815))    # ➞ ["o o", "@", "- - -"]
print(maya_number(16125))  # ➞ ["o o", "@", "o -", "-"]
