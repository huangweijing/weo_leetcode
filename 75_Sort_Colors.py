from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0, 1, 2]
        color_cnt = [0] * len(colors)
        for num in nums:
            color_cnt[num] += 1
        idx = 0
        for color in colors:
            for i in range(color_cnt[color]):
                nums[idx] = color
                idx += 1

data = [0, 1, 2, 2, 1]
Solution().sortColors(data)
print(data)



