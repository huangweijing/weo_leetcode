from typing import List
from collections import Counter

class Solution:
    def __init__(self):
        self.word_cnt = dict[str, Counter]()
        self.letter_cnt = Counter()
        self.scores = dict[str, int]()
        self.dp = dict[str, int]()
        self.words = []

    def key(self, letters: Counter) -> str:
        result = ""
        for k, v in letters.items():
            result += str(k) + str(v)
        return result

    def my_score(self, letters: Counter) -> int:
        key = self.key(letters)
        if key in self.dp:
            return self.dp[key]
        max_score = 0
        words = self.words.copy()
        for word in words:
            if self.word_cnt[word] < letters:
                self.words.remove(word)
                max_score = max(max_score, self.my_score(letters - self.word_cnt[word]) + self.scores[word])
                self.words.append(word)
        self.dp[key] = max_score
        return max_score

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.words = words
        for word in words:
            cnt = Counter(word)
            self.word_cnt[word] = cnt
            s = 0
            for k, v in cnt.items():
                s += score[ord(k) - ord("a")] * v
            self.scores[word] = s
        self.letter_cnt = Counter(letters)
        return self.my_score(self.letter_cnt)

data = [
["add","dda","bb","ba","add"]
, ["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d"]
, [3,9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
r = Solution().maxScoreWords(* data)
print(r)

