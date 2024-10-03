from typing import List
from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = Counter()
        for num in arr:
            cnt[num % k] += 1
        if cnt[0] & 1 == 1:
            return False
        for i in range(1, k // 2 + 1):
            if cnt[i] != cnt[k - i]:
                return False
        return True
        