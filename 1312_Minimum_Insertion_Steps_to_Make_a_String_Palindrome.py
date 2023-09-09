from functools import cache

class Solution:

    def __init__(self):
        self.s = ""
        self.cnt = 0
        self.ans = 0

    @cache
    def my_sol(self, l1: int, r1: int, l2: int, r2: int):
        # self.cnt += 1
        if r1 == l1 and l2 == r2:
            return 0
        if r1 == l1:
            return r2 - l2
        if r2 == l2:
            return r1 - l1
        if self.s[l1] == self.s[r2]:
            return self.my_sol(l1 + 1, r1, l2, r2 - 1)
        else:
            sol1 = self.my_sol(l1 + 1, r1, l2, r2) + 1
            sol2 = self.my_sol(l1, r1, l2, r2 - 1) + 1
            return min(sol1, sol2)

    def minInsertions(self, s: str) -> int:
        self.s = s
        self.ans = len(s)
        for i, ch in enumerate(s):
            sol1 = self.my_sol(0, i, i, len(s) - 1)
            sol2 = self.my_sol(0, i, i - 1, len(s) - 1)
            ans = min(self.ans, sol1, sol2)
        # print(self.cnt)
        return ans

# data = "rvnrababpgimhbcczhjeeaukyzwabvwmjdjwlsocjjcegumiyninfefchykopgjfvnwxpfxsaxgbbrqgkuwifzlcfdzgfibaygjzzdzzyhpltvgjghzupfslyxtmzjchprofiyynjmbsbvsjfwffcugmjyqqgviciravehvpqdgcxlzxn"
data = "leetcode"
r = Solution().minInsertions(data)
print(r)