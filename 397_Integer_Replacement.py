class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n & 1 == 1:
            n1 = self.integerReplacement(n + 1) + 1
            n2 = self.integerReplacement(n - 1) + 1
            return min(n1, n2)
        else:
            return self.integerReplacement(n >> 1) + 1

r = Solution().integerReplacement(8)
print(r)