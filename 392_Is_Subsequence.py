class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s = 0
        idx = 0
        while idx_s < len(s):
            while idx < len(t) and t[idx] != s[idx_s]:
                idx += 1
            if idx == len(t):
                return False
            idx += 1
            idx_s += 1
        return True

s = "aaaaaaaa"
t = "bbaaaaaa"
r = Solution().isSubsequence(s, t)
print(r)