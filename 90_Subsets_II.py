from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        subsets_n_1 = self.subsets(nums[1:])
        result = list[list[int]]()
        key_set = set[str]()
        for s in subsets_n_1:
            new_set = s.copy()
            new_set.append(nums[0])

            key = self.get_key(s)
            if key not in key_set:
                result.append(s)
                key_set.add(key)

            key = self.get_key(new_set)
            if key not in key_set:
                result.append(new_set)
                key_set.add(key)
        return result

    def get_key(self, num_list: list[int]):
        num_list.sort()
        key = "_"
        for idx in range(len(num_list)):
            key += str(num_list[idx]) + "_"
        return key

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.subsets(nums)



sol = Solution()
r = sol.subsetsWithDup([4,4,4,1,4])
print(r)