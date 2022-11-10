from typing import List
from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        sorted_nums = SortedList(nums.copy())
        for n in nums:
            sorted_nums.remove(n)
            if len(stk) == 0:
                stk.append(n)
            elif n < stk[-1]:
                stk.append(n)
            else:
                n1 = stk[-1]
                n2 = n
                idx1 = sorted_nums.bisect_right(n1)
                idx2 = sorted_nums.bisect_left(n2)
                # print(n1, n2, sorted_nums, idx1, idx2)
                if idx1 < idx2:
                    return True
        return False

data = [9,12,10,4]
r = Solution().find132pattern(data)
print(r)