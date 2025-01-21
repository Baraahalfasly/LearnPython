def eratosthenes(n):
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
                
    return [i for i in range(2, n + 1) if sieve[i]]

# Test cases
print(eratosthenes(1))  # ➞ []
print(eratosthenes(10)) # ➞ [2, 3, 5, 7]
print(eratosthenes(20)) # ➞ [2, 3, 5, 7, 11, 13, 17, 19]
print(eratosthenes(0))  # ➞ []
