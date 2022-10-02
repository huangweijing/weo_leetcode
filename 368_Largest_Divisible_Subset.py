from typing import List
from sortedcontainers import SortedDict

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        np = SortedDict()
        lst_dict = dict[int, list[int]]()
        result = []
        for num in nums:
            lst = []
            for key, val in np.items():
                if num % key == 0:
                    if val > len(lst):
                        lst = lst_dict[key]
            # print(num, lst)
            lst = lst.copy()
            lst.append(num)
            lst_dict[num] = lst
            np[num] = len(lst)

            if len(lst) > len(result):
                result = lst
        return result

data_nums = [1,2,4,6,12,18,36,8]
r = Solution().largestDivisibleSubset(data_nums)
print(r)
