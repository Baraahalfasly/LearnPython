def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        # Optimization to stop checking divisors above sqrt(n)
        if divisor * divisor > n and n > 1:
            factors.append(n)
            break
    return factors

# Examples
print(prime_factors(20))       # ➞ [2, 2, 5]
print(prime_factors(100))      # ➞ [2, 2, 5, 5]
print(prime_factors(8912234))  # ➞ [2, 47, 94811]
