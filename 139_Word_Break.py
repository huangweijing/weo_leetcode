from typing import List
from collections import Counter
from functools import cache

class Solution:
    def __init__(self):
        self.word_dict = set[str]()

    @cache
    def my_word_break(self, s) -> bool:
        if s in self.word_dict:
            return True
        for i in range(1, len(s)):
            if s[: i] in self.word_dict:
                # print(s[:i], s[i:])
                if self.my_word_break(s[i: ]):
                    return True
        return False

    def check_valid(self, s: str, wordDict: List[str]) -> bool:
        s_set = set(s)
        w_set = set("".join(wordDict))
        n_set = s_set.intersection(w_set)
        if len(s_set) > len(n_set):
            return False
        else:
            return True

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not self.check_valid(s, wordDict):
            return False
        self.word_dict = set(wordDict)
        return self.my_word_break(s)

data_s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# data_wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
data_wordDict = ["aa","aaa","ba"]
r = Solution().wordBreak(data_s, data_wordDict)
print(r)