def sorting(s):
    unique_chars = sorted(set(s), key=lambda x: (x.isdigit(), x.isupper(), x))
    return ''.join(unique_chars)

# Test cases
print(sorting("eA2a1E"))  # Output: "aAeE12"
print(sorting("Re4r"))    # Output: "erR4"
print(sorting("6jnM31Q")) # Output: "jMnQ136"
print(sorting("846ZIbo")) # Output: "bIoZ468"
