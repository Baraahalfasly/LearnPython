import math

def decipher_square(s):
    # Remove spaces to determine the core message
    s = s.replace(" ", "")
    
    # Determine the grid size (smallest possible square)
    n = math.ceil(math.sqrt(len(s)))
    
    # Fill the grid row-wise
    grid = []
    index = 0
    for i in range(n):
        grid.append(s[index:index+n])
        index += n

    # Read column-wise
    deciphered_text = ''.join(''.join(row[i] for row in grid if i < len(row)) for i in range(n))
    
    return deciphered_text

# Test cases
print(decipher_square("Ms ussahr nHaaib"))  # Mubashir Hassan
print(decipher_square("Eisadng  tm    i   zbia a"))  # Edabit is amazing
print(decipher_square("acer"))  # acre
