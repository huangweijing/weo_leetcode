from functools import cache


class Solution:
    @cache
    def distance(self, ch1: str, ch2: str):
        return min((ord(ch1) - ord(ch2) + 26) % 26, (ord(ch2) - ord(ch1) + 26) % 26)

    def getSmallestString(self, s: str, k: int) -> str:
        ans = ""
        for ch in s:
            dist_a = self.distance(ch, "a")
            if self.distance(ch, "a") <= k:
                ans += "a"
                k -= dist_a
            else:
                ans += chr(ord(ch) - k)
                k = 0
        return ans




