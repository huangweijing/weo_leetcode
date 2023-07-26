from typing import List
from sortedcontainers import SortedList

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left = SortedList([nums[0]])
        right = SortedList(nums[1:])
        if left[-1] <= right[0]:
            return 1
        # print(left, right)
        for i, num in enumerate(nums[1:]):
            left.add(num)
            right.remove(num)
            # print(left, right)
            if left[-1] <= right[0]:
                return i + 2
        return -1


data = [1,1,1,0,6,12]
r = Solution().partitionDisjoint(data)
print(r)