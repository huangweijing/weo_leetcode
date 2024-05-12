from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter((s1 + " " + s2).split(" "))
        return [k for k, v in cnt.items() if v == 1]
