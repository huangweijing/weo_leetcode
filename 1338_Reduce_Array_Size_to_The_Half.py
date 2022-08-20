from typing import List
from functools import cache

class Solution:
    @cache
    def minSetSize(self, arr: List[int]) -> int:
        num_dict = dict[int, int]()
        for num in arr:
            if num not in num_dict:
                num_dict[num] = 0
            num_dict[num] += 1
        val_list = list(num_dict.values())
        val_list.sort(reverse=True)
        result = 0
        val_sum = 0
        for val in val_list:
            val_sum += val
            result += 1
            if val_sum >= (len(arr) / 2):
                return result
        return result

from collections import Counter
c = Counter([1, 2, 3, 4, 2, 1, 3])
print(c[23])