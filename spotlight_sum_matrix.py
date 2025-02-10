def spotlight_map(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Function to calculate sum of neighbors (including itself)
    def spotlight_sum(r, c):
        total = 0
        for i in range(max(0, r - 1), min(rows, r + 2)):
            for j in range(max(0, c - 1), min(cols, c + 2)):
                total += grid[i][j]
        return total
    
    # Construct the result matrix
    return [[spotlight_sum(r, c) for c in range(cols)] for r in range(rows)]

# Test cases
print(spotlight_map([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))  # ➞ [[12, 21, 16], [27, 45, 33], [24, 39, 28]]

print(spotlight_map([
  [2, 6, 1, 3, 7],
  [8, 5, 9, 4, 0]
]))  # ➞ [[21, 31, 28, 24, 14], [21, 31, 28, 24, 14]]

print(spotlight_map([[3]]))  # ➞ [[3]]
