from typing import List

def rwh_primes1(n: int):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = rwh_primes1(n)
        prime_set = set[int](primes)
        ans = []
        for prime in primes:
            if prime <= n - prime and n - prime in prime_set:
                ans.append([prime, n - prime])
        return ans

r = Solution().findPrimePairs(100)
print(r)
