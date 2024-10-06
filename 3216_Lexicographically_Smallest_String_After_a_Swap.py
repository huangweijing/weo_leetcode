class Solution:
    def getSmallestString(self, s: str) -> str:
        ans = ""
        for i, ch in enumerate(s):
            if i > 0:
                if int(s[i - 1]) & 1 == int(s[i]) & 1 and s[i - 1] > s[i]:
                    ans += s[:i - 1]
                    ans += s[i] + s[i - 1]
                    ans += s[i + 1:]
                    return ans
        return s
