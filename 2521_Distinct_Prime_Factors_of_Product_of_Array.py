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
    primes = rwh_primes1(1000)

    def factorize(self, num: int) -> set[int]:
        fact_set = set[int]()
        idx = 0
        while num > 1:
            while num % Solution.primes[idx] == 0:
                fact_set.add(Solution.primes[idx])
                num //= Solution.primes[idx]
            idx += 1
        return fact_set

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        fact_set = set[int]()
        for num in nums:
            fs = self.factorize(num)
            for f in fs:
                fact_set.add(f)
        return len(fact_set)
    
data = [2,4,3,7,10,6]
r = Solution().distinctPrimeFactors(data)
print(r)