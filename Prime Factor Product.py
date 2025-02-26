def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def product_of_primes(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # i is a factor
            j = n // i
            if is_prime(i) and is_prime(j):  # Check if both factors are prime
                return True
    return False

# Test cases
print(product_of_primes(2059))  # True
print(product_of_primes(10))    # True
print(product_of_primes(25))    # True
print(product_of_primes(999))   # False
