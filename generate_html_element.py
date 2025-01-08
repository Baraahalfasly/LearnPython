def secret(input_str):
    # Split the input into tag and class parts
    parts = input_str.split(".")
    tag = parts[0]
    classes = " ".join(parts[1:])
    
    # Construct and return the HTML string
    return f"<{tag} class='{classes}'></{tag}>"

# Examples
print(secret("p.one.two.three"))  # "<p class='one two three'></p>"
print(secret("p.one"))            # "<p class='one'></p>"
print(secret("p.four.five"))      # "<p class='four five'></p>"
