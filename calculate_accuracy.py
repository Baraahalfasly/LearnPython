def mark_maths(equations):
    correct_count = 0  # Number of correct equations
    total_count = len(equations)  # Total number of equations
    
    for eq in equations:
        # Split the equation into the problem and the expected result
        problem, result = eq.split('=')
        try:
            # Evaluate the left-hand side and compare it with the expected result
            if eval(problem) == int(result):  
                correct_count += 1
        except Exception:
            pass  # Ignore any invalid equations
    
    # Calculate the percentage of correct equations
    percentage = (correct_count / total_count) * 100
    return f"{round(percentage)}%"

# Examples
print(mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]))  # "75%"
print(mark_maths(["1-2=-2"]))  # "0%"
print(mark_maths(["2+3=5", "4+4=9", "3-1=2"]))  # "67%"
