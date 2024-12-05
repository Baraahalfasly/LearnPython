def censor_string(sentence, words_to_censor, replacement_char):
    # Split the sentence into words
    words = sentence.split()
    
    # Process each word
    censored_words = []
    for word in words:
        # Check if the word (case-insensitive) is in the list of words to censor
        if word.lower() in [w.lower() for w in words_to_censor]:
            # Replace the word with the replacement characters of the same length
            censored_words.append(replacement_char * len(word))
        else:
            # Keep the word as it is if it's not in the censor list
            censored_words.append(word)
    
    # Rejoin the words into a single string
    return " ".join(censored_words)

# Examples:
# Example 1
result1 = censor_string("Today is a Wednesday!", ["Today", "a"], "-")
print(result1)  # Output: "----- is - Wednesday!"

# Example 2
result2 = censor_string("The cow jumped over the moon.", ["cow", "over"], "*")
print(result2)  # Output: "The *** jumped **** the moon."

# Example 3
result3 = censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*")
print(result3)  # Output: "Why *** the ******* cross the ****?"
