def remove_letters(letters, word):
    for char in word:
        if char in letters:
            letters.remove(char)
    return letters

# Test cases
print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))  # ➞ ["w"]
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))  # ➞ ["b", "g", "w"]
print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))  # ➞ []
