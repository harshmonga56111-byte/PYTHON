#sum of prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = int(input("Enter limit: "))
prime_sum = sum(i for i in range(2, limit+1) if is_prime(i))
print("Sum of primes =", prime_sum)
