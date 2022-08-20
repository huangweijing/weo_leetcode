from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = dict[int, int]()
        for i, num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = list[int]()
            num_dict[num].append(i)
        for key in num_dict:
            idx_list = num_dict[key]
            if len(idx_list) > 1:
                for i in range(1, len(idx_list)):
                    if idx_list[i] - idx_list[i - 1] <= k:
                        return True
        return False

