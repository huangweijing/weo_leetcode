from functools import cache

class Solution:
    def __init__(self):
        self.dp = dict[str, dict[str, str]]()


    def my_diverse_str(self, a: int, b: int, c: int) -> list[str]:
        pass


    # @cache
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a > 0:
            self.longestDiverseString(a - 1, b, c)


