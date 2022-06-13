from typing import List
from collections import deque

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        num_set = set[int]()
        num_queue: deque[int] = deque[int]()
        maximum = -1
        num_sum = 0
        for num in nums:
            if num not in num_set:
                num_set.add(num)
                num_queue.append(num)
                num_sum += num
            else:
                while True:
                    n = num_queue.popleft()
                    if n != num:
                        num_set.remove(n)
                        num_sum -= n
                    else:
                        num_queue.append(n)
                        break

            if num_sum > maximum:
                maximum = num_sum
            # print(nums, num_set, num_queue)

        return maximum

sol = Solution()
r = sol.maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434])
print(r)
