def max_score(s):
    max_score = 0  # Store the highest score
    
    for i in range(1, len(s)):  # Avoid splitting at the first or last position
        left = s[:i]   # Left part
        right = s[i:]  # Right part
        score = left.count('0') + right.count('1')  # Calculate score
        max_score = max(max_score, score)  # Update maximum score
    
    return max_score

# Test cases
print(max_score("00111"))  # 5
print(max_score("1111"))   # 3
print(max_score("01001"))  # 4
print(max_score("010101010101010101"))  # 10
