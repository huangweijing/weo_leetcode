from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        subsets_n_1 = self.subsets(nums[1:])
        result = list[list[int]]()
        # result.append([nums[0]])
        for s in subsets_n_1:
            new_set = s.copy()
            new_set.append(nums[0])
            result.append(s)
            result.append(new_set)
        return result

r = Solution().subsets([1, 2, 3])
print(r)