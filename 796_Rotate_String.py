class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(1, len(s)):
            if goal == s[i:] + (s[:i:-1]):
                return True
        return False
