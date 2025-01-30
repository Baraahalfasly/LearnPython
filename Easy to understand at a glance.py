def same_vowel_group(words):
    vowels = set('aeiou')
    
    def word_vowels(word):
        return set(char for char in word if char in vowels)
    
    if not words:
        return []
    
    first_word_vowels = word_vowels(words[0])
    return [word for word in words if word_vowels(word) == first_word_vowels]

# Test the function
print(same_vowel_group(["toe", "ocelot", "maniac"]))
print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))
print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))
