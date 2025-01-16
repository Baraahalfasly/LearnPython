from collections import Counter

def find_the_difference(s, t):
    # Count the frequency of characters in both strings
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Find the character with a different frequency in 't'
    for char in count_t:
        if count_t[char] != count_s.get(char, 0):
            return char

# Test cases
print(find_the_difference("abcd", "abcde"))  # ➞ "e"
print(find_the_difference("", "y"))          # ➞ "y"
print(find_the_difference("ae", "aea"))      # ➞ "a"
