from typing import List
from collections import defaultdict

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_list = [[num, i] for i, num in enumerate(nums)]
        sorted_list.sort()
        ans = [0] * len(nums)
        num_group = [sorted_list[0]]
        for i, num_val in enumerate(sorted_list[1: ], start=1):
            if num_val[0] - limit <= sorted_list[i - 1][0]:
                num_group.append(num_val)
            else:
                val_list, idx_list = [], []
                for val in num_group:
                    val_list.append(val[0])
                    idx_list.append(val[1])
                idx_list.sort()
                for j, idx in enumerate(idx_list):
                    ans[idx] = val_list[j]
                num_group = [num_val]
        val_list, idx_list = [], []
        for val in num_group:
            val_list.append(val[0])
            idx_list.append(val[1])
        idx_list.sort()
        for j, idx in enumerate(idx_list):
            ans[idx] = val_list[j]
        return ans

data = [
    [1,5,3,9,8]
    , 2
]
r = Solution().lexicographicallySmallestArray(*data)
print(r)
