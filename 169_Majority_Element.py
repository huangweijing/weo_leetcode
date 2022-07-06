from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_cnt = dict[int, int]()
        for num in nums:
            if num in num_cnt.keys():
                num_cnt[num] += 1
            else:
                num_cnt[num] = 1
        result = -1
        max_key = -1
        for key in num_cnt.keys():
            if num_cnt[key] > max_key:
                max_key = num_cnt[key]
                result = key
        return result



