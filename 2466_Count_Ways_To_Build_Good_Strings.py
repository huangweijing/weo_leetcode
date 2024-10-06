class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[one] = 1
        dp[zero] += 1
        for i in range(len(dp)):
            if dp[i] > 0:
                if i + one <= high:
                    dp[i + one] = (dp[i] + dp[i + one]) % mod
                if i + zero <= high:
                    dp[i + zero] = (dp[i] + dp[i + zero]) % mod
        return sum(dp[low:]) % mod