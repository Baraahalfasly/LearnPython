def secret(input_string):
    # Split the input string into parts using the dot as a delimiter
    parts = input_string.split('.')
    # The first part is the HTML tag
    tag = parts[0]
    # The remaining parts are the classes, joined with spaces
    classes = ' '.join(parts[1:])  # Combine classes with spaces
    # Return the formatted HTML string
    return f"<{tag} class='{classes}'></{tag}>"

# Examples of using the function
print(secret("p.one.two.three"))  # Output: "<p class='one two three'></p>"
print(secret("p.one"))           # Output: "<p class='one'></p>"
print(secret("p.four.five"))     # Output: "<p class='four five'></p>"
