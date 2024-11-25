class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(1, n):
            new_dp = [0] * 5
            for j, _ in enumerate(dp):
                new_dp[j] = sum(dp[:j + 1])
            dp = new_dp
        return sum(dp)
    

r = Solution().countVowelStrings(2)
print(r)