def can_see_stage(matrix):
    # Transpose the matrix to work with columns as rows
    columns = zip(*matrix)
    
    # Check each column
    for column in columns:
        # Check if each row in the column is strictly increasing
        if not all(column[i] < column[i+1] for i in range(len(column) - 1)):
            return False
    return True

# Test cases
print(can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))  # True

print(can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))  # True

print(can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]))  # False

print(can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))  # False
