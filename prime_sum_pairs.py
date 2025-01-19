def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_pair_list(n):
    # Step 1: Generate all primes less than or equal to n
    primes = [p for p in range(2, n + 1) if is_prime(p)]
    
    # Step 2: Find prime pairs that sum to n
    pairs = []
    for p in primes:
        complement = n - p
        if complement >= p and complement in primes:
            pairs.append(f"{p}+{complement}")
    
    return pairs

# Test cases
print(prime_pair_list(10))  # ➞ ["3+7", "5+5"]
print(prime_pair_list(50))  # ➞ ["3+47", "7+43", "13+37", "19+31"]
print(prime_pair_list(100)) # ➞ ["3+97", "11+89", "17+83", "29+71", "41+59", "47+53"]
