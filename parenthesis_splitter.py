def split(string):
    result = []
    current = ""
    count = 0
    
    for char in string:
        current += char
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        
        if count == 0:
            result.append(current)
            current = ""
    
    return result

# Test the function
print(split("()()()"))  # ["()", "()", "()"]
print(split("((()))"))  # ["((()))"]
print(split("((()))(())()()(()())"))  # ["((()))", "(())", "()", "()", "(()())"]
print(split("((())())(()(()()))"))  # ["((())())", "(()(()()))"]
