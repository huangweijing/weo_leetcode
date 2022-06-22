class Solution:
    def __init__(self):
        self.dp = [None] * 20
        self.dp[1] = 1
        self.dp[0] = 1

    def numTrees(self, n: int) -> int:
        if self.dp[n] is not None:
            return self.dp[n]
        sol_cnt = 0
        for i in range(n):
            sol_cnt += self.numTrees(i) * self.numTrees(n - 1 - i)
        self.dp[n] = sol_cnt
        return sol_cnt

sol = Solution()
r = sol.numTrees(8)
print(r)