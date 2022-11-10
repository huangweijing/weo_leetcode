from functools import cache
class Solution:
    def __init__(self):
        self.s = ""

    @cache
    def my_sol(self, left: int, right: int):
        if left > right:
            return 0
        if left == right:
            return 1
        if self.s[left] == self.s[right]:
            return self.my_sol(left + 1, right - 1) + 2
        else:
            return max(self.my_sol(left + 1, right)
                       , self.my_sol(left, right - 1))

    def longestPalindromeSubseq(self, s: str) -> int:
        self.s = s
        return self.my_sol(0, len(s) - 1)



data = "bbbab"
r = Solution().longestPalindromeSubseq(data)
print(r)