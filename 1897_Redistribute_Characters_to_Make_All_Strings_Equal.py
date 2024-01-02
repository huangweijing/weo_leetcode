from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = Counter()
        for word in words:
            cnt += Counter(word)
        for val in cnt.values():
            if val % len(words) != 0:
                return False
        return True


