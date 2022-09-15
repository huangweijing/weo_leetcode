import bisect
import math
from math import sqrt
class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        max_num = int(sqrt(n))
        for i in range(2, max_num + 1):
            if n % i == 0:
                return False
        return True

    def numPrimeArrangements(self, n: int) -> int:
        prime_nums = [i for i in range(2, n + 1) if self.is_prime(i)]
        print(prime_nums)
        result = math.factorial(len(prime_nums)) * math.factorial(n - len(prime_nums))
        return result % (10 ** 9 + 7)

r = Solution().numPrimeArrangements(2)
print(r)
