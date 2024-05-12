from typing import List
from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = Counter(num)
        for i, ch in enumerate(num):
            if not str(cnt[str(i)]) == ch:
                return False
        return True
