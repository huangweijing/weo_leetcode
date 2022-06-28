class Solution:
    def __init__(self):
        self.dp = dict[str, bool]()

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 + s2 in self.dp.keys():
            return self.dp[s1 + s2]

        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if s1[0] != s3[0] and s2[0] != s3[0]:
            return False
        if s1[-1] != s3[-1] and s2[-1] != s3[-1]:
            return False
        r1 = False
        r2 = False
        if s1[0] == s3[0]:
            r1 = self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
            r2 = self.isInterleave(s1, s2[1:], s3[1:])
        self.dp[s1 + s2] = r1 or r2
        return r1 or r2

sol = Solution()
r = sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")
print(r)

