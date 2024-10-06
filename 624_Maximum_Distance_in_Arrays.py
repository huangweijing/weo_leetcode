from typing import List
from collections import Counter
import math


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cnt = Counter()
        key_list = []
        for arr in arrays:
            cnt[arr[-1]] += 1
            cnt[arr[0]] += 1
            key_list.append(arr[-1])
            key_list.append(arr[0])
        key_list.sort()
        ans = 0
        for arr in arrays:
            if key_list[-1] == arr[-1] and cnt[arr[-1]] == 1:
                max_val = key_list[-2]
            else:
                max_val = key_list[-1]
            if key_list[0] == arr[0] and cnt[arr[0]] == 1:
                min_val = key_list[0]
            else:
                min_val = key_list[1]
            ans = max(ans, max_val - min_val)
        return ans
