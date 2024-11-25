from typing import List
from collections import Counter


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        arr_dict = Counter()
        for i, num in enumerate(nums):
            if i >= len(nums) // 2:
                break
            num2 = nums[-1 - i]
            two_range = [2, limit * 2]
            one_range = [min(num, num2) + 1, max(num, num2) + limit]
            zero = num + num2
            arr_dict[two_range[0]] += 2
            arr_dict[two_range[1] + 1] -= 2 
            arr_dict[one_range[0]] -= 1
            arr_dict[one_range[1] + 1] += 1
            arr_dict[zero] -= 1
            arr_dict[zero + 1] += 1
            print(zero, one_range, two_range)
            # print([[key, arr_dict[key]] for key in sorted(arr_dict)])
        keys = list(sorted(arr_dict.keys()))
        ans = 2 * len(nums)
        cost = 0
        for key in keys[:-1]:
            cost += arr_dict[key]
            ans = min(ans, cost)
            # print(key, cost, arr_dict[key])
        return ans
    
data = [
    [3,4,3,3]
    , 4
]
r = Solution().minMoves(*data)
print(r)
        
