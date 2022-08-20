from typing import List
from collections import Counter
from functools import cache

class Solution:
    def __init__(self):
        self.word_dict = set[str]()

    @cache
    def my_word_break(self, s) -> list[str]:
        result = list[str]()
        if s in self.word_dict:
            result.append(s)
        for i in range(1, len(s)):
            if s[: i] in self.word_dict:
                sub_result = self.my_word_break(s[i: ])
                for sub in sub_result:
                    result.append(s[:i] + " " + sub)
        return result

    def check_valid(self, s: str, wordDict: List[str]) -> bool:
        s_set = set(s)
        w_set = set("".join(wordDict))
        n_set = s_set.intersection(w_set)
        if len(s_set) > len(n_set):
            return False
        else:
            return True

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not self.check_valid(s, wordDict):
            return []
        self.word_dict = set(wordDict)
        return self.my_word_break(s)

data_s = "pineapplepenapple"
data_wordDict = ["apple","pen","applepen","pine","pineapple"]
r = Solution().wordBreak(data_s, data_wordDict)
print(r)