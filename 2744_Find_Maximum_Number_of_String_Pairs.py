from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        word_set = set[str]()
        for word in words:
            if word[1] + word[0] in word_set:
                ans += 1
            word_set.add(word)
        return ans