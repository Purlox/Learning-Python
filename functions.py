def prime(prime_num):
    """Returns the Xth prime number or -1 on a wrong argument."""
    if prime_num < 1:
        return -1

    possible_prime = 3
    found_primes = [2]

    while len(found_primes) < prime_num:
        for prime in found_primes:
            if possible_prime % prime == 0:
                break
        else:
            found_primes.append(possible_prime)

        possible_prime += 1

    return found_primes[-1]


def fibonacci(fib_num):
    """Returns the Xth fib number."""
    if fib_num == 0:
        return 0
    elif fib_num == 1:
        return 1
    elif fib_num > 1:
        return fibonacci(fib_num - 1) + fibonacci(fib_num - 2)


def factorial(fact_num):
    """Returns factorial of the argument"""
    if fact_num == 0:
        return 1
    elif fact_num > 0:
        return fact_num * factorial(fact_num - 1)


def power(base, exponent=2):
    """Returns the power of the base."""
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)


def my_min(number1, number2):
    """Returns the smaller number of the two numbers."""
    return (number1 + number2) / 2 - abs((number1 - number2) / 2)


def my_max(number1, number2):
    """Returns the smaller number of the two numbers."""
    return (number1 + number2) / 2 + abs((number1 - number2) / 2)


# "*numbers" means variable amount of arguments
def my_sum(*numbers):
    """Returns the sum of ALL the numbers."""
    sum = 0

    for num in numbers:
        sum += num

    return sum


# "**numbers" means variable amount of arguments called using keywords like
# test=3 or name="Student"
def write_args(**keywords):
    """Writes the arguments and keywords used to call the function."""
    keys = sorted(keywords.keys())

    for key in keys:
        print(key, "=", keywords[key])


def rng(init):
    """Returns a 'random' number generator function."""
    return lambda n: n * init + init