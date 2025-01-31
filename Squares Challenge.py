def tic_tac_toe(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != "E":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "E":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "E":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "E":
        return board[0][2]
    
    # If no winner, check for draw or ongoing game
    if any("E" in row for row in board):
        return "Ongoing"
    else:
        return "Draw"

# Test cases
test_cases = [
    ([["X", "O", "X"],
      ["O", "X", "O"],
      ["O", "X", "X"]], "X"),
    
    ([["O", "O", "O"],
      ["O", "X", "X"],
      ["E", "X", "X"]], "O"),
    
    ([["X", "X", "O"],
      ["O", "O", "X"],
      ["X", "X", "O"]], "Draw"),
    
    ([["X", "E", "O"],
      ["E", "O", "X"],
      ["E", "X", "E"]], "Ongoing"),
    
    ([["X", "O", "X"],
      ["X", "O", "O"],
      ["X", "X", "O"]], "X")
]

# Run test cases
for i, (board, expected) in enumerate(test_cases, 1):
    result = tic_tac_toe(board)
    print(f"Test case {i}:")
    for row in board:
        print(row)
    print(f"Expected: {expected}")
    print(f"Result: {result}")
    print("Pass" if result == expected else "Fail")
    print()
