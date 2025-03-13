from typing import List


def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [0, 10e9]
        found = False
        primes = rwh_primes(right + 1)
        print(primes)
        for i, prime in enumerate(primes):
            if left <= prime <= right and i + 1 < len(primes) \
                and left <= primes[i + 1] <= right:
                if primes[i + 1] - primes[i] < ans[1] - ans[0]:
                    ans = [primes[i], primes[i + 1]]
                    found = True
        if not found:
            return [-1, -1]
        return ans
    
r = Solution().closestPrimes(2, 1000000)
print(r)
