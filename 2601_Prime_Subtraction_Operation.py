from typing import List
from collections import deque
import bisect


class Solution:
    @classmethod
    def rwh_primes(cls, n):
        """ Returns  a list of primes < n """
        sieve = [True] * n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
        return [2] + [i for i in range(3, n, 2) if sieve[i]]

    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = deque(Solution.rwh_primes(1001))
        low_val = 0
        for num in nums:
            if low_val >= num:
                return False
            idx = bisect.bisect_left(primes, num - low_val) - 1
            if idx != -1:
                prime = primes[idx]
                low_val = num - prime
            else:
                low_val = num
        return True

# print(Solution.rwh_primes(1001))
data = [5,8,3]
r = Solution().primeSubOperation(data)
print(r)



