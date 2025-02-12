def diagonalize(n, direction):
    matrix = [[i + j for j in range(n)] for i in range(n)]
    
    if direction == "ul":
        return matrix
    elif direction == "ur":
        return [row[::-1] for row in matrix]
    elif direction == "ll":
        return matrix[::-1]
    elif direction == "lr":
        return [row[::-1] for row in matrix[::-1]]

# Test cases
print(diagonalize(3, "ul"))  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
print(diagonalize(4, "ur"))  # [[3, 2, 1, 0], [4, 3, 2, 1], [5, 4, 3, 2], [6, 5, 4, 3]]
print(diagonalize(3, "ll"))  # [[2, 3, 4], [1, 2, 3], [0, 1, 2]]
print(diagonalize(5, "lr"))  # [[8, 7, 6, 5, 4], [7, 6, 5, 4, 3], [6, 5, 4, 3, 2], [5, 4, 3, 2, 1]]
