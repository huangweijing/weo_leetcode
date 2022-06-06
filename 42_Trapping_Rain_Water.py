from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_from_left = [0] * len(height)
        max_from_right = [0] * len(height)
        max_val = -1
        idx = 0
        while idx < len(height):
            if height[idx] > max_val:
                max_val = height[idx]
            max_from_left[idx] = max_val
            idx += 1

        max_val = -1
        idx = len(height) - 1
        while idx >= 0:
            if height[idx] > max_val:
                max_val = height[idx]
            max_from_right[idx] = max_val
            idx -= 1
        # print(height)
        # print(max_from_right)
        # print(max_from_left)
        contain = 0
        for i in range(len(height)):
            max_height = max_from_left[i] if max_from_left[i] < max_from_right[i] else max_from_right[i]
            if height[i] < max_height:
                contain += max_height - height[i]
        return contain

sol = Solution()
r = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(r)


