import math


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int(math.sqrt(2 * target + 1 / 4) - 1 / 2)
        v1 = target - (n * (n + 1) // 2)
        v2 = ((n + 2) * (n + 1) // 2) - target
        print(n, v1, v2)
        return min(n + v1 * 2, n + 1 + v2 * 2)

r = Solution().reachNumber(4)
print(r)