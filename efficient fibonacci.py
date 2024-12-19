def fib_fast(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test cases
print(fib_fast(5))   # ➞ 5
print(fib_fast(10))  # ➞ 55
print(fib_fast(20))  # ➞ 6765
print(fib_fast(50))  # ➞ 12586269025
