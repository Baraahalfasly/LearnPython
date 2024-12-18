from collections import Counter

def anagram(name, words):
    # Normalize the name (remove spaces and convert to lowercase)
    name = name.replace(" ", "").lower()
    
    # Normalize the list of words (convert to lowercase and concatenate)
    combined_words = "".join(words).lower()
    
    # Count characters in the name and the combined words
    name_count = Counter(name)
    words_count = Counter(combined_words)
    
    # Check if the counts match
    return name_count == words_count

# Test cases
print(anagram("Justin Bieber", ["injures", "ebb", "it"]))  # True
print(anagram("Natalie Portman", ["ornamental", "pita"]))  # True
print(anagram("Chris Pratt", ["chirps", "rat"]))           # False
print(anagram("Jeff Goldblum", ["jog", "meld", "bluffs"])) # False
