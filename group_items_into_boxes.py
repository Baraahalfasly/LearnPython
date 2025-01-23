def boxes(weights):
    box_count = 0
    current_weight = 0
    
    # Sort the weights to attempt packing from smallest to largest
    weights.sort()
    
    for weight in weights:
        if current_weight + weight <= 10:  # Add the weight to the current box if under limit
            current_weight += weight
        else:
            # Start a new box
            box_count += 1
            current_weight = weight  # Set the current weight to the current item
    
    # Account for the last box
    if current_weight > 0:
        box_count += 1
    
    return box_count

# Test with the given list
print(boxes([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]))  # Output should be 5
