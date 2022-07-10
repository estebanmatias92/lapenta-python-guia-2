#
#   Return a list with all the primes numbers between 2 to num
#
def sieve_of_eratosthenes(num):
    # Initialize the sieve
    primes = []
    composites = []

    # Range limits
    MIN = 2
    MAX = num + 1

    # Exit if the number is too small
    if num < MIN:
        return primes

    for i in range(MIN, MAX):
        # If number is not in the sieve, add it to the list of primes
        if i not in composites:
            primes.append(i)

            # Update the list of composite numbers
            for j in range(i * i, MAX, i):
                composites.append(j)

    return primes
