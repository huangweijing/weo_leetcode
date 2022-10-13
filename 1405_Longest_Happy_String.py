from functools import cache

class Solution:
    def __init__(self):
        self.dp = dict[str, dict[str, str]]()


    def my_diverse_str(self, a: int, b: int, c: int) -> list[str]:
        result = []
        sub_result = []
        if a > 0:
            sub = self.longestDiverseString(a - 1, b, c)
            for s in sub:
                if sub[-2:] != "aa":
                    result.append(s + "a")
        if b > 0:
            sub = self.longestDiverseString(a, b - 1, c)
            for s in sub:
                if sub[-2:] != "bb":
                    result.append(s + "a")
        if c > 0:
            sub = self.longestDiverseString(a, b, c - 1)
            for s in sub:
                if sub[-2:] != "cc":
                    result.append(s + "a")


    # @cache
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a > 0:
            self.longestDiverseString(a - 1, b, c)


