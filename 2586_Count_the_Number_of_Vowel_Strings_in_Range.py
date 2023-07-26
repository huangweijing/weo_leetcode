from typing import List
from collections import Counter

class Solution:
    def vowelStrings(self, words: List[str]
                     , left: int, right: int) -> int:
        ans = 0
        vow_set = set[int](["a", "i", "u", "e", "o"])
        for i in range(left, right + 1):
            if words[i][0] in vow_set and words[i][-1] in vow_set:
                ans += 1
        return ans
