def restore_vowels(text, vowels):
    """
    Replaces the asterisks (*) in the given text with the vowels provided in the correct order.
    
    Parameters:
    text (str): The string containing asterisks (*) where vowels should be restored.
    vowels (str): The string of vowels to insert into the text.

    Returns:
    str: The text with asterisks replaced by vowels.
    """
    # Convert vowels into an iterator for sequential replacement
    vowels = iter(vowels)
    # Replace '*' with the next vowel, or keep the character as is
    return ''.join(next(vowels) if char == '*' else char for char in text)

# Examples:
# Example 1
result1 = restore_vowels("Wh*r* d*d my v*w*ls g*?", "eeioeo")
print(result1)  # Output: "Where did my vowels go?"

# Example 2
result2 = restore_vowels("abcd", "")
print(result2)  # Output: "abcd"

# Example 3
result3 = restore_vowels("*PP*RC*S*", "UEAE")
print(result3)  # Output: "UPPERCASE"
