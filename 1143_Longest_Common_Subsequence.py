from functools import cache

class Solution:
    def __init__(self):
        self.text1 = ""
        self.text2 = ""

    @cache
    def my_lcs(self, len1: int, len2: int):
        if len1 == 0 or len2 == 0:
            return 0
        if self.text1[len1 - 1] == self.text2[len2 - 1]:
            return self.my_lcs(len1 - 1, len2 - 1) + 1
        else:
            return max(self.my_lcs(len1, len2 - 1), self.my_lcs(len1 - 1, len2))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1, self.text2 = text1, text2
        return self.my_lcs(len(self.text1), len(self.text2))

