def nearest_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Find the position of the letter in the alphabet (1-indexed)
    letter_pos = ord(letter) - ord('a')
    # Compute distances to each vowel
    distances = {vowel: abs(letter_pos - (ord(vowel) - ord('a'))) for vowel in vowels}
    # Find the vowel with the smallest distance
    return min(distances, key=distances.get)

# Test cases
print(nearest_vowel("b"))  # ➞ "a"
print(nearest_vowel("s"))  # ➞ "u"
print(nearest_vowel("c"))  # ➞ "a"
print(nearest_vowel("i"))  # ➞ "i"
