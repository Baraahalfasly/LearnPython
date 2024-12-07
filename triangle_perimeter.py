import math

def perimeter(vertices):
    # Extract coordinates
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    
    # Calculate distances between vertices
    d1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    d2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    d3 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    
    # Calculate the perimeter
    perimeter = d1 + d2 + d3
    
    # Round the result to 2 decimal places
    return round(perimeter, 2)

# Test cases
print(perimeter([[15, 7], [5, 22], [11, 1]]))    # 47.08
print(perimeter([[0, 0], [0, 1], [1, 0]]))      # 3.41
print(perimeter([[-10, -10], [10, 10], [-10, 10]])) # 68.28
