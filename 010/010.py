def sum_of_primes_below(limit):
    if limit < 2:
        return 0
    
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    
    for current in range(2, int(limit ** 0.5) + 1):
        if sieve[current]:
            sieve[current*current : limit : current] = [False] * len(sieve[current*current : limit : current])
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return sum(primes)

result = sum_of_primes_below(2_000_000)
print("A soma dos primos abaixo de 2 milhões é:", result)