class Solution:
    def countVowelStrings(self, n: int) -> int:
        # vowels = ["aeiou"]
        dp = [[0] * 5 for i in range(2)]
        dp[0] = [1, 1, 1, 1, 1]
        for i in range(1, n):
            dp[1][0] = dp[0][0]
            dp[1][1] = dp[0][0] + dp[0][1]
            dp[1][2] = dp[0][0] + dp[0][1] + dp[0][2]
            dp[1][3] = dp[0][0] + dp[0][1] + dp[0][2] + dp[0][3]
            dp[1][4] = dp[0][0] + dp[0][1] + dp[0][2] + dp[0][3] + dp[0][4]
            dp[0] = dp[1].copy()
        return sum(dp[0])
