from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        val_dict = defaultdict(lambda : list[int]())
        for i, num in enumerate(nums):
            val_dict[num].append(i)
        # print(val_dict)
        ans = [0] * len(nums)
        for val_list in val_dict.values():
            if len(val_list) == 1:
                continue
            # print(val_list)
            left = 0
            right = sum([val_list[i] - val_list[0] for i in range(1, len(val_list))])
            ans[val_list[0]] = right
            # print(left, right)
            for i in range(1, len(val_list)):
                # jump from i to i + 1
                distance = val_list[i] - val_list[i - 1]
                left += i * distance
                right -= (len(val_list) - i) * distance
                # print(i, left, right)
                ans[val_list[i]] = left + right
        return ans
                    

        # print(val_dict)

data = [1,3,1,1,2]
r = Solution().distance(data)
print(r)