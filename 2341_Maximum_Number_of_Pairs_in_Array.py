from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        num_set = set[int]()
        pair_cnt = 0
        for num in nums:
            if num in num_set:
                num_set.remove(num)
                pair_cnt += 1
            else:
                num_set.add(num)
        return [pair_cnt, len(num_set)]
