def get_frame(width, height, char):
    # Check if the width or height is less than or equal to 2
    if width <= 2 or height <= 2:
        return "invalid"
    
    # Create the top and bottom borders
    top_bottom = char * width
    
    # Create the middle rows (with spaces in the middle)
    middle = char + " " * (width - 2) + char
    
    # Combine all rows into the frame
    frame = [top_bottom] + [middle] * (height - 2) + [top_bottom]
    
    # Return the frame as a list of lists (each row in its own list)
    return [[row] for row in frame]

# Examples of usage
print(get_frame(4, 5, "#"))
print(get_frame(10, 3, "*"))
print(get_frame(2, 5, "0"))
