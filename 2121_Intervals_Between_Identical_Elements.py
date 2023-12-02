from typing import List
from collections import Counter


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        ans = []
        num_sum_right = Counter()
        num_cnt_right = Counter()
        num_sum_left = Counter()
        num_cnt_left = Counter()
        for i, num in enumerate(arr):
            num_sum_right[num] += i
            num_cnt_right[num] += 1
        for i, num in enumerate(arr):
            num_sum_right[num] -= i
            num_cnt_right[num] -= 1
            left = i * num_cnt_left[num] - num_sum_left[num]
            right = num_sum_right[num] - i * num_cnt_right[num]
            ans.append(left + right)
            num_sum_left[num] += i
            num_cnt_left[num] += 1
        return ans

data = [2,1,3,1,2,3,3]
r = Solution().getDistances(data)
print(r)
