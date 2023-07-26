from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter = Counter()
        for word in words:
            hash_val = 0
            for ch in word:
                idx = ord(ch) - ord("a")
                hash_val |= 1 << idx
            counter[hash_val] += 1
        ans = 0
        for val in counter.values():
            ans += val * (val - 1) // 2
        return ans
