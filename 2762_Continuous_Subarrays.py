from typing import List
from sortedcontainers import SortedList


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sorted_list = SortedList()
        ans = 0
        for i, num in enumerate(nums):
            sorted_list.add(num)
            diff = abs(sorted_list[0] - sorted_list[-1])
            if diff <= 2:
                ans += len(sorted_list)
            else:
                while diff > 2:
                    # print(f"nums={nums}, diff={diff}, remove {nums[i - len(sorted_list) + 1]}")
                    sorted_list.remove(nums[i - len(sorted_list) + 1])
                    # print(f"nums={nums}, sorted_list after remove {sorted_list}")
                    diff = abs(sorted_list[0] - sorted_list[-1])
                ans += len(sorted_list)
        return ans


data = [5,4,2,4]
r = Solution().continuousSubarrays(data)
print(r)

# s = SortedList([2, 3, 4, 2])
# print(s)
