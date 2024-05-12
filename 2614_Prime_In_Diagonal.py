def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        prime_set = set(rwh_primes(4 * 10 ** 6))
        ans = 0
        for i in range(len(nums)):
            if nums[i][i] in prime_set:
                ans = max(ans, nums[i][i])
            if nums[i][-1 - i] in prime_set:
                ans = max(ans, nums[i][-1 - i])
        return ans
