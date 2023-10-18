from typing import List
from collections import Counter
import bisect


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        idle_cnt = 0
        for val in cnt.values():
            if val > 1:
                idle_cnt += val - 1
        num_list = list(cnt.keys())
        num_list.sort()
        # print(num_list, len(nums))
        min_shortage = len(nums)
        for i, num in enumerate(num_list):
            idx = bisect.bisect_left(num_list, num + len(nums) - 1)
            if idx < len(num_list) and num_list[idx] == num + len(nums) - 1:
                idx += 1
            shortage_cnt = len(nums) - (idx - i)
            min_shortage = min(min_shortage, shortage_cnt)
            # print(i, num + len(nums) - 1, (idx - i), shortage_cnt)
        return min_shortage

data = [1,10,100,1000]
r = Solution().minOperations(data)
print(r)
