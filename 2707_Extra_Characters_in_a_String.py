from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.word_set = set[int]()
        self.s = ""

    @cache
    def in_dict(self, left: int, right: int) -> bool:
        return self.s[left: right + 1] in self.word_set

    # def my_sol(self, left: int, right: int):
    #     for i in range(left, right + 1):
    #         if self.in_dict(left, i)


    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.s = s
        for word in dictionary:
            self.word_set.add(word)
