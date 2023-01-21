from typing import List
from functools import cache


class Solution:
    def __init__(self):
        self.nums = []

    @staticmethod
    def get_key(nums: list[int]):
        return ".".join(map(str, nums))

    @cache
    def get_seq(self, idx: int) -> list[list[int]]:
        ans = list[list[int]]()
        num = self.nums[idx]
        ans.append([num])
        for i in range(idx + 1, len(self.nums)):
            if self.nums[i] >= num:
                sub_ans = self.get_seq(i)
                for sub in sub_ans:
                    seq = [num]
                    seq.extend(sub.copy())
                    ans.append(seq)
        return ans

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        key_set = set()
        ans = []
        for i in range(len(nums)):
            sub_ans = self.get_seq(i)
            for sub in sub_ans:
                if len(sub) > 1:
                    key = Solution.get_key(sub)
                    if key not in key_set:
                        ans.append(sub)
                        key_set.add(key)
        return ans

r = Solution().findSubsequences([4,6,7,7])
print(r)
