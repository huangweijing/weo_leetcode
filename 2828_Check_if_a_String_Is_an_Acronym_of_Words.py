from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return len(words) == len(s) and len([i for i, ch in enumerate(s) if words[i][0] != ch]) == 0