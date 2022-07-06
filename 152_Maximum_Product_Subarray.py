from typing import List

class Solution:
    def __init__(self):
        self.min_pdt = []
        self.max_pdt = []

    # max mps ending end of nums
    def max_min_product(self, nums: list[int], end_idx: int ) -> (int, int):
        if end_idx == 0:
            # print("hello")
            self.max_pdt[end_idx] = nums[0]
            self.min_pdt[end_idx] = nums[0]
            return nums[0], nums[0]

        if self.max_pdt[end_idx] is not None and self.min_pdt[end_idx] is not None :
            return self.max_pdt[end_idx], self.min_pdt[end_idx]

        max_n_1, min_n_1 = self.max_min_product(nums, end_idx - 1)
        if nums[end_idx] > 0:
            max_result = max_n_1 * nums[end_idx]
            min_result = min_n_1 * nums[end_idx]
            if nums[end_idx] > max_result:
                max_result = nums[end_idx]
            if nums[end_idx] < min_result:
                min_result = nums[end_idx]
        elif nums[end_idx] < 0:
            max_result = min_n_1 * nums[end_idx]
            min_result = max_n_1 * nums[end_idx]
            if nums[end_idx] > max_result:
                max_result = nums[end_idx]
            if nums[end_idx] < min_result:
                min_result = nums[end_idx]
        else:
            max_result = 0
            min_result = 0

        self.max_pdt[end_idx] = max_result
        self.min_pdt[end_idx] = min_result

        return max_result, min_result


    def maxProduct(self, nums: List[int]) -> int:
        self.max_pdt = [None] * len(nums)
        self.min_pdt = [None] * len(nums)
        max_product = - 2 ** 31
        for i in range(0, len(nums)):
            ma, mi = self.max_min_product(nums, i)
            # print(self.max_pdt)
            # print(self.min_pdt)

            if ma > max_product:
                max_product = ma
        return max_product




sol = Solution()
data = [-2]
r = sol.maxProduct(data)
print(r)