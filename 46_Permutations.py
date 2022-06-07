from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        num = nums.pop()
        n_1_results = self.permute(nums)
        # print(n_1_results)
        results = list[list[int]]()
        for n_1_result in n_1_results:
            for i in range(len(n_1_result) + 1):
                result = n_1_result.copy()
                result.insert(i, num)
                results.append(result)

        return results


sol = Solution()
r = sol.permute([0, 1])
print(r)

