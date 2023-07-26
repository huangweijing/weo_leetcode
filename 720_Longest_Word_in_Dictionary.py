from typing import List
from functools import cache


class Solution:
    def __init__(self):
        self.word_dict = dict[str, int]()
        self.words = list[str]()

    @cache
    def my_sol(self, idx: int) -> bool:
        ans = False
        word = self.words[idx]
        if word[:-1] == "":
            ans = True
        elif word[:-1] in self.word_dict:
            ans = self.my_sol(self.word_dict[word[:-1]])
        return ans

    def longestWord(self, words: List[str]) -> str:
        self.word_dict = { word: i for i, word in enumerate(words) }
        self.words = words
        ans = ""
        for i, word in enumerate(self.words):
            if self.my_sol(i):
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans):
                    if word < ans:
                        ans = word
        return ans


data = ["a","banana","app","appl","ap","apply","apple"]
r = Solution().longestWord(data)
print(r)
