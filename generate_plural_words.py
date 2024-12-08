def pluralize(words):
    # Create a dictionary to count the occurrences of each word
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1  # Increment count for each word
    
    # Create a set to store the final result
    result = set()
    for word, count in word_counts.items():
        if count > 1:  # If the word appears more than once
            result.add(word + "s")  # Add the plural form
        else:  # If the word appears only once
            result.add(word)
    
    return result

# Test the function
print(pluralize(["cow", "pig", "cow", "cow"]))  # ➞ {"cows", "pig"}
print(pluralize(["table", "table", "table"]))   # ➞ {"tables"}
print(pluralize(["chair", "pencil", "arm"]))    # ➞ {"chair", "pencil", "arm"}
