import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        max_num = int(math.sqrt(n)) + 1
        primes = [0] * n
        primes[2] = 0
        for i in range(2, max_num):
            if primes[i] == 1:
                continue
            k = 0
            j = (i + k) * i
            while j < n:
                primes[j] = 1
                k += 1
                j = (i + k) * i
        return len([i for i in range(2, n) if primes[i] == 0])

r = Solution().countPrimes(1000000)
print(r)







