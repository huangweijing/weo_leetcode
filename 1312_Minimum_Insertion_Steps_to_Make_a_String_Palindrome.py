from functools import cache

class Solution:

    def __init__(self):
        self.s = ""
        self.cnt = 0
        self.ans = 0

    @cache
    def my_sol(self, left: int, right: int):
        # print(left, right)
        if left >= right:
            return 0
        elif self.s[left] == self.s[right]:
            return self.my_sol(left + 1, right - 1)
        else:
            sub1 = self.my_sol(left + 1, right)
            sub2 = self.my_sol(left, right - 1)
            return min(sub1, sub2) + 1

    def minInsertions(self, s: str) -> int:
        self.s = s
        return self.my_sol(0, len(s) - 1)

# data = "rvnrababpgimhbcczhjeeaukyzwabvwmjdjwlsocjjcegumiyninfefchykopgjfvnwxpfxsaxgbbrqgkuwifzlcfdzgfibaygjzzdzzyhpltvgjghzupfslyxtmzjchprofiyynjmbsbvsjfwffcugmjyqqgviciravehvpqdgcxlzxn"
data = "leetcode"
r = Solution().minInsertions(data)
print(r)