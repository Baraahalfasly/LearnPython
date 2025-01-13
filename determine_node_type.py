def node_type(nodes, parents, target):
    # Check if the target node exists
    if target not in nodes:
        return "Not exist"
    
    # Find the index of the target node
    target_index = nodes.index(target)
    
    # Check if the target is a root node
    if parents[target_index] == -1:
        return "Root"
    
    # Check if the target is a leaf node
    if target not in parents:
        return "Leaf"
    
    # If not root or leaf, it must be an inner node
    return "Inner"

# Test cases
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5))  # "Root"
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6))  # "Leaf"
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2))  # "Inner"
print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10)) # "Not exist"
