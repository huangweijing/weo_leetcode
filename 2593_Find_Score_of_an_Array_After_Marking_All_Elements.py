from typing import List
from collections import defaultdict

class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [0] * len(nums)
        num_dict = defaultdict(lambda : list[int]())
        for i, num in enumerate(nums):
            num_dict[num].append(i)
        keys = list(num_dict.keys())
        keys.sort()
        ans = 0
        for key in keys:
            pos_list = num_dict[key]
            for pos in pos_list:
                if marked[pos] == 1:
                    continue
                marked[pos] = 1
                ans += key
                if pos > 0:
                    marked[pos - 1] = 1
                if pos < len(nums) - 1:
                    marked[pos + 1] = 1
        return ans

data = [2,3,5,1,3,2]
r = Solution().findScore(data)
print(r)