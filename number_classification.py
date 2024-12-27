def sum_of_divisors(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

def num_type(n):
    # Check if the number is Perfect
    if sum_of_divisors(n) == n:
        return "Perfect"
    
    # Check if the number is Amicable
    for i in range(1, n):
        if sum_of_divisors(i) == n and sum_of_divisors(n) == i:
            return "Amicable"
    
    return "Neither"

# Test cases
print(num_type(6))    # ➞ "Perfect"
print(num_type(2924)) # ➞ "Amicable"
print(num_type(5010)) # ➞ "Neither"
