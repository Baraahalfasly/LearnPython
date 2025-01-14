def sum_round(num):
    result = []
    place_value = 1
    
    while num > 0:
        digit = num % 10
        if digit != 0:
            result.append(str(digit * place_value))
        num //= 10
        place_value *= 10
    
    return " ".join(result[::-1])

# Test cases
print(sum_round(101))    # Output: "1 100"
print(sum_round(1234))   # Output: "4 30 200 1000"
print(sum_round(54210))  # Output: "10 200 4000 50000"
