from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter()
        num_list = []
        for num in arr:
            cnt[num] += 1
            if cnt[num] == 1:
                num_list.append(num)
        for num in num_list:
            if cnt[num] == 1:
                k -= 1
            if k == 0:
                return num
        return ""


