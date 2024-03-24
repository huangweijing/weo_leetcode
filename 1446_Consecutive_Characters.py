class Solution:
    def maxPower(self, s: str) -> int:
        idx = 0
        ch = s[idx]
        ans = 0
        while idx < len(s):
            str_len = 0
            while idx < len(s) and s[idx] == ch:
                idx += 1
                str_len += 1
            if idx < len(s):
                ch = s[idx]
            ans = max(ans, str_len)
        return ans
