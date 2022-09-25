import math

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        result = 0
        for i in range(1, n + 1):
            result = (result << int(math.log2(i) + 1)) + i
            result = result % mod
        return result % mod

r = Solution().concatenatedBinary(100000)
print(r)
