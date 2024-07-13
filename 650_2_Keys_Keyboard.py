def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [1, 2] + [i for i in range(3, n, 2) if sieve[i]]


class Solution:
    def minSteps(self, n: int) -> int:
        primes = rwh_primes(n + 1)
        ans = 0
        while n > 1:
            while n % primes[-1] != 0:
                primes.pop()
            n //= primes[-1]
            ans += primes[-1]
        return ans


r = Solution().minSteps(100)
print(r)
        
