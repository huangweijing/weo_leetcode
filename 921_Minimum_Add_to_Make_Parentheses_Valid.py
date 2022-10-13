from collections import Counter

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        pcnt = 0
        ans = 0
        for ch in s:
            if ch == "(":
                pcnt += 1
            else:
                pcnt -=1
            if pcnt < 0:
                ans += 1
                pcnt = 0
        ans += pcnt
        return ans

