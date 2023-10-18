class Solution:
    MOD = 10 ** 9 + 7
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [0] * 1000
        dp[0] = 1
        for i in range(steps):
            # print(dp)
            new_dp = [0] * len(dp)
            for j in range(len(new_dp)):
                # print(dp)
                new_dp[j] = dp[j]
                if j - 1 >= 0:
                    new_dp[j] = (dp[j - 1] + new_dp[j]) % Solution.MOD
                if j + 1 < min(len(new_dp), arrLen):
                    new_dp[j] = (dp[j + 1] + new_dp[j]) % Solution.MOD
            dp = new_dp
        return dp[0]

r = Solution().numWays(500, 100000)
print(r)
