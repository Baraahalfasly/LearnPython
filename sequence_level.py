def sequence_level(*numbers):
    def calculate_differences(sequence):
        # Calculate differences between consecutive elements in the sequence
        return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

    level = 0  # Level of the sequence
    current_sequence = list(numbers)  # Start with the given sequence
    
    while len(current_sequence) > 1:
        level += 1  # Move to the next level
        differences = calculate_differences(current_sequence)  # Calculate differences
        if all(difference == differences[0] for difference in differences):  # Check if all differences are equal
            if level == 1:
                return "Linear"
            elif level == 2:
                return "Quadratic"
            elif level == 3:
                return "Cubic"
            else:
                return f"{level}-th degree"
        current_sequence = differences  # Move to the next level of differences

    return "Unknown"

# Examples:
print(sequence_level(1, 2, 3, 4, 5))          # ➞ "Linear"
print(sequence_level(3, 6, 10, 15, 21))      # ➞ "Quadratic"
print(sequence_level(4, 14, 40, 88, 164))    # ➞ "Cubic"
