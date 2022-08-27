class Solution:
    def __init__(self):
        self.np = [0] * 60
        self.np[1] = 1

    def integerBreak(self, n: int) -> int:
        if self.np[n] > 0:
            return self.np[n]
        for i in range(1, (n + 1 >> 1) + 1):
            self.np[n] = max(self.np[n], self.integerBreak(i) * self.integerBreak(n - i)
                             , self.integerBreak(i) * (n - i)
                             , self.integerBreak(n - i) * i
                             , i * (n - i))

        return self.np[n]

r = Solution().integerBreak(58)
print(r)