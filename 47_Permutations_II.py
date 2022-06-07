from typing import List

class Solution:

    def calc_hash(self, nums: List[int]):
        idx = 0
        hash_code = 0
        while idx < len(nums):
            hash_code += (nums[idx] + 20) ** idx
            idx += 1
        return hash_code

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        num = nums.pop()
        n_1_results = self.permuteUnique(nums)
        results = list[list[int]]()
        hash_set = set[int]()
        for n_1_result in n_1_results:
            for i in range(len(n_1_result) + 1):
                result = n_1_result.copy()
                result.insert(i, num)
                hc = self.calc_hash(result)
                if hc not in hash_set:
                    hash_set.add(hc)
                    results.append(result)

        return results

sol = Solution()
r = sol.permuteUnique([1,1,1])
print(r)