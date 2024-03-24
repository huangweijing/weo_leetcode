from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words[i + 1:], start=i + 1):
                if word2[: len(word1)] == word1 and word2[-len(word1): ] == word1:
                    ans += 1
        return ans


