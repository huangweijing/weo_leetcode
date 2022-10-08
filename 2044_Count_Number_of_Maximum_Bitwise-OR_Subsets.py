import functools
from typing import List
from collections import Counter

class Solution:
    max_bit = 17
    def __init__(self):
        self.cnt = Counter()
        self.result = 0
        self.dp = dict[str, list[list[int]]]()

    def my_hash(self, nums: list[int]) -> str:
        return ".".join(map(str, nums))

    def permuate(self, nums: list[int]) -> list[list[int]]:
        key = self.my_hash(nums)
        if key in self.dp:
            return self.dp[key].copy()
        if len(nums) == 1:
            self.dp[key] = [nums.copy()]
            return self.dp[key]

        result = list[list[int]]()
        # for i in range(1, len(nums)):
        result.append([nums[0]])
        arr = nums[1:].copy()
        sub_result = self.permuate(arr)
        # print(key, nums[0], arr, sub_result)
        result.extend(sub_result.copy())
        for sub in sub_result:
            sub = sub.copy()
            sub.append(nums[0])
            result.append(sub)

        self.dp[key] = result.copy()
        return result

    def or_all(self, nums: list[int]):
        return functools.reduce(lambda a, b: a | b, nums)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # for num in nums:
        #     for i in range(Solution.max_bit):
        #         self.cnt[i] += (num >> i) & 1
        result = 0
        max_num = self.or_all(nums)
        permutations = self.permuate(nums)
        for p in permutations:
            if self.or_all(p) == max_num:
                result += 1
        return result

r = Solution().countMaxOrSubsets(list(range(17)))
print(r)
