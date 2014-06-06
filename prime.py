# Finds the Xth prime number

prime_num = 10  # The Xth prime to find and print.

possible_prime = 3
found_primes = [2]

while len(found_primes) < prime_num:
    for prime in found_primes:
        if possible_prime % prime == 0:
            break
    else:
        found_primes.append(possible_prime)

    possible_prime += 1

print(prime_num, "th prime is", found_primes[prime_num - 1])
