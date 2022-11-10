from functools import cache

class Solution:

    def __init__(self):
        self.s = ""

    @cache
    def is_palindromic(self, sta: int, end: int) -> bool:
        if end < sta:
            return False
        if sta == end:
            return True
        if self.s[sta] == self.s[end] and\
                (self.is_palindromic(sta + 1, end - 1) or sta + 1 == end):
            return True
        return False

    def countSubstrings(self, s: str) -> int:
        self.s = s
        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindromic(i, j):
                    ans += 1
        return ans