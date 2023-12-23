import functools


class Solution:
    def maxScore(self, s: str) -> int:
        right_score = sum(1 if ch == "1" else 0 for ch in s)
        left_score = 0
        ans = 0
        for ch in s[:-1]:
            left_score += 1 if ch == "0" else 0
            right_score -= 1 if ch == "1" else 0
            ans = max(ans, left_score + right_score)
        return ans