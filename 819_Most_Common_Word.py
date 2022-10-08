from typing import List
from collections import Counter
import math

class Solution:
    def __init__(self):
        self.paragraph = ""
        self.idx = 0

    def read(self) -> str:
        word = ""
        while self.idx < len(self.paragraph) and self.paragraph[self.idx] in "!?',;. ":
            self.idx += 1
        while self.idx < len(self.paragraph) and self.paragraph[self.idx] not in "!?',;. ":
            word += self.paragraph[self.idx]
            self.idx += 1
        return word

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        self.paragraph = paragraph.lower()
        banned = set(banned)
        cnt = Counter()
        max_cnt = [-math.inf, ""]
        while True:
            word = self.read()
            if word == "":
                break
            if word not in banned:
                cnt[word] += 1
                if cnt[word] > max_cnt[0]:
                    max_cnt = [cnt[word], word]
        return max_cnt[1]

data_para = "a b b."
data_banned = ["b"]
r = Solution().mostCommonWord(data_para, data_banned)
print(r)
