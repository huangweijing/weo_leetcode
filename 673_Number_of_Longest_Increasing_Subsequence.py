from typing import List
from functools import cache
from collections import Counter

class Solution:
    def __init__(self):
        self.nums = []

    @cache
    def my_sol(self, idx: int) -> (int, int):
        # if idx == 0:
        #     return 1, 1
        num = self.nums[idx]
        ret_len, ret_size = 1, 1
        for i in range(idx):
            if self.nums[i] < num:
                length, size = self.my_sol(i)
                if length + 1 > ret_len:
                    ret_size = size
                    ret_len = length + 1
                elif length + 1 == ret_len:
                    ret_size = size + ret_size
        # print(idx, self.nums[idx], ret_len, ret_size)
        return ret_len, ret_size


    def findNumberOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        cnt = Counter()
        for i in range(len(nums)):
            sub_len, sub_size = self.my_sol(i)
            cnt[sub_len] += sub_size
        key_list = list(cnt.keys())
        key_list.sort(reverse=True)
        return cnt[key_list[0]]



data = [2,2,2]
r = Solution().findNumberOfLIS(data)
print(r)

