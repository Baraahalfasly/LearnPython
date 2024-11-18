def encrypt(word):
    # Step 1: Reverse the string
    reversed_word = word[::-1]
    
    # Step 2: Replace vowels
    vowel_map = {'a': '0', 'e': '1', 'o': '2', 'u': '3'}
    transformed_word = ''.join(vowel_map[char] if char in vowel_map else char for char in reversed_word)
    
    # Step 3: Add "aca" to the end
    encrypted_word = transformed_word + "aca"
    
    return encrypted_word

# Test cases
print(encrypt("banana"))  # Output: "0n0n0baca"
print(encrypt("karaca"))  # Output: "0c0r0kaca"
print(encrypt("burak"))   # Output: "k0r3baca"
print(encrypt("alpaca"))  # Output: "0c0pl0aca"
