from typing import List
from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        ans = 0
        for i, num in enumerate(nums):
            if num == 1:
                arr[i] = arr[i - 1] + 1
            else:
                arr[i] = arr[i - 1] - 1
            # print(arr)
            if arr[i] == 0:
                ans = i + 1

        max_min_dict = defaultdict(lambda : [10 ** 6, -1])
        for i, num in enumerate(arr):
            if i < max_min_dict[num][0]:
                max_min_dict[num][0] = i
            if i > max_min_dict[num][1]:
                max_min_dict[num][1] = i
        # print(max_min_dict)
        for val in max_min_dict.values():
            ans = max(ans, val[1] - val[0])
        return ans

data = [
    0,1,0
]
r = Solution().findMaxLength(data)
print(r)



