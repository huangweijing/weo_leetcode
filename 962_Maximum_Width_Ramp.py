from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        left_right_dict = dict[int, list[int]]()
        for idx, num in enumerate(nums):
            if num not in left_right_dict:
                left_right_dict[num] = [idx, idx]
            else:
                left_right_dict[num] = [min(idx, left_right_dict[num][0])
                    , max(idx, left_right_dict[num][1])]
        keys = list(left_right_dict.keys())
        keys.sort(reverse=True)
        ans = -1
        max_idx = -1
        for i, key in enumerate(keys):
            min_idx = left_right_dict[key][0]
            max_idx = max(max_idx, left_right_dict[key][1])
            ans = max(max_idx - min_idx, ans)
        return ans

data = [9,8,1,0,1,9,4,0,4,1]
r = Solution().maxWidthRamp(data)
print(r)
