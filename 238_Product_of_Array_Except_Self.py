import functools
from typing import List
from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_cnt = Counter(nums)
        if num_cnt[0] > 1:
            return [0] * len(nums)
        elif num_cnt[0] == 1:
            arr = [0] * len(nums)
            zero_idx = nums.index(0)
            all_product = 1
            for num, cnt in num_cnt.items():
                if num == 0:
                    continue
                all_product *= (num ** cnt)
            arr[zero_idx] = all_product
            return arr
        else:
            all_product = functools.reduce(lambda a, b: a*b, nums)
            return list(map(lambda x: int(all_product / x), nums))
