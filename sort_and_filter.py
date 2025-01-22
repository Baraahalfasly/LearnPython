def sorting(s):
    # Separate characters and digits
    letters = [char for char in s if char.isalpha()]
    digits = [char for char in s if char.isdigit()]
    
    # Remove duplicates from letters and sort them case-insensitively
    letters = sorted(set(letters), key=lambda x: (x.lower(), x))
    
    # Sort digits
    digits = sorted(digits)
    
    # Join letters and digits and return
    return ''.join(letters) + ''.join(digits)

# Test cases
print(sorting("eA2a1E"))  # ➞ "aAeE12"
print(sorting("Re4r"))     # ➞ "erR4"
print(sorting("6jnM31Q"))  # ➞ "jMnQ136"
print(sorting("846ZIbo"))  # ➞ "bIoZ468"
