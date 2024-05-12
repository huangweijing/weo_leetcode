class Solution:
    def countKeyChanges(self, s: str) -> int:
        last = s[0].lower()
        ans = 0
        for ch in s[1:]:
            if last != ch.lower():
                ans += 1
            last = ch.lower()
        return ans
