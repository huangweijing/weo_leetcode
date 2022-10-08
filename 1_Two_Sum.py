from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        num_dic = defaultdict(lambda : [])
        for i, num in enumerate(nums):
            num_dic[num].append(i)
        # print(num_dic)
        for i, num in enumerate(nums):
            idx_list = num_dic[target - num]
            for idx in idx_list:
                if idx == i:
                    continue
                return [idx, i]
        return result

data_nums = [3,2,4]
data_target = 5
res = Solution().twoSum(data_nums, data_target)
print(res)

# num_dic = defaultdict(lambda: [])
# num_dic[2].append(2)
# num_dic[2].append(3)
# print(num_dic)
