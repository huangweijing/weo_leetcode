class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        dp_last, dp = 1, 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                dp = dp_last + 1
            else:
                dp = 1
            ans = max(ans, dp)
            dp_last = dp
        return ans