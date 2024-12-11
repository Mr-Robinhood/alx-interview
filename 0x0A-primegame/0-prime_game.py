#!/usr/bin/python3

def isWinner(x, nums):
    def sieve_of_eratosthenes(max_n):
        """Generate a list indicating prime status for numbers up to max_n."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    def count_primes(n, prime_sieve):
        """Count the number of primes up to n."""
        return sum(prime_sieve[:n + 1])

    # Edge case: If no rounds are played, return None
    if x < 1 or not nums:
        return None

    # Precompute primes up to the largest number in nums
    max_n = max(nums)
    prime_sieve = sieve_of_eratosthenes(max_n)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = count_primes(n, prime_sieve)
        # Maria wins if the number of primes is odd; Ben wins otherwise
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))

