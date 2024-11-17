def atbash(text):
    result = []  # List to store the transformed (encoded) characters
    for char in text:  # Iterate through each character in the input text
        if char.isalpha():  # Check if the character is alphabetic (a-z, A-Z)
            if char.islower():  # If the character is lowercase
                # Calculate the transformed character using the formula: ord('a') + ord('z') = 219
                result.append(chr(219 - ord(char)))
            elif char.isupper():  # If the character is uppercase
                # Calculate the transformed character using the formula: ord('A') + ord('Z') = 155
                result.append(chr(155 - ord(char)))
        else:
            # Non-alphabetic characters (e.g., spaces, digits, punctuation) are kept as they are
            result.append(char)
    return ''.join(result)  # Join the list of characters into a single string and return it

# Test cases
print(atbash("apple"))  # ➞ "zkkov"
print(atbash("Hello world!"))  # ➞ "Svool dliow!"
print(atbash("Christmas is the 25th of December"))  # ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
