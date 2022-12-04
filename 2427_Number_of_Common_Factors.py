class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, min(a, b) + 1):
            if a % i == b % i == 0:
                ans += 1
        return ans
