from typing import List

class Solution:
    def __init__(self):
        self.calc_all_dp = dict[str,int]()

    def calc(self, pre_result: int, nums: list[int], target:int) -> int:
        key = str(pre_result) + "," + ".".join(map(str, nums))
        if key in self.calc_all_dp:
            return self.calc_all_dp[key]
        if len(nums) == 0:
            if pre_result == target:
                return 1
            else:
                return 0
        result = 0
        result += self.calc(pre_result + nums[0], nums[1:], target)
        result += self.calc(pre_result - nums[0], nums[1:], target)
        self.calc_all_dp[key] = result
        return result

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.calc(0, nums, target)

data_nums = [25,29,23,21,45,36,16,35,13,39,44,15,16,14,45,23,50,43,9,15]
data_target = 32
r = Solution().findTargetSumWays(data_nums, data_target)
print(r)
# print(list(filter(lambda t: t % 2 == 0, data_nums)))