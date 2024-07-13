class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        people = 0
        for ch in s:
            people += 1 if ch == "E" else -1
            ans = max(ans, people)
        return ans
