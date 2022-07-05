class Solution:
    def __init__(self):
        self.dp = dict[str, int]()
        self.alp_set = set()
        for i in range(1, 27):
            self.alp_set.add(str(i))
            if i >= 11 and i != 20:
                self.dp[str(i)] = 2
            else:
                self.dp[str(i)] = 1

    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if s in self.dp.keys():
            return self.dp[s]

        cnt = 0
        if s[-2:] in self.alp_set:
            cnt += self.numDecodings(s[:-2])
        if s[-1:] in self.alp_set:
            cnt += self.numDecodings(s[:-1])

        self.dp[s] = cnt

        return cnt

sol = Solution()
r = sol.numDecodings("06")
print(r)