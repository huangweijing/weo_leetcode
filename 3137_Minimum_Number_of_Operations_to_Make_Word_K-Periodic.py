from collections import Counter


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        word_cnt = Counter()
        for i in range(len(word) // k):
            word_cnt[word[i * k: (i + 1) * k]] += 1
        return len(word) // k - max(word_cnt.values())
