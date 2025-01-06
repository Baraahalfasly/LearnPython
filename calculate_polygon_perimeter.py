import math

def perimeter(vertices):
    total_perimeter = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]  # Connect last point to first
        total_perimeter += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(total_perimeter, 2)

# Test cases
print(perimeter([[15, 7], [5, 22], [11, 1]]))  # ➞ 47.08
print(perimeter([[0, 0], [0, 1], [1, 0]]))     # ➞ 3.41
print(perimeter([[-10, -10], [10, 10], [-10, 10]]))  # ➞ 68.28
