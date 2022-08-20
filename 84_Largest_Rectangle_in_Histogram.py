from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        left_gt_idx_arr = [-1] * len(heights)
        right_gt_idx_arr = [-1] * len(heights)

        sta = []
        sta_idx = []
        for i in range(len(heights)):
            idx = None
            val = None
            while len(sta) > 0 and sta[-1] >= heights[i]:
                val = sta.pop()
                idx = sta_idx.pop()
            left_gt_idx_arr[i] = idx
            # if heights[i] == val:
            #     sta.append(val)
            #     sta_idx.append(idx)
            # else:
            sta.append(heights[i])
            sta_idx.append(i)

        sta = []
        sta_idx = []
        for i in range(len(heights) - 1, -1, -1):
            idx = None
            val = None
            while len(sta) > 0 and sta[-1] >= heights[i]:
                val = sta.pop()
                idx = sta_idx.pop()
                # print(f"poping..{val}")
            print(heights[i], heights,sta)
            right_gt_idx_arr[i] = idx
            # if heights[i] == val:
            #     sta.append(val)
            #     sta_idx.append(idx)
            # else:
            sta.append(heights[i])
            sta_idx.append(i)
        # right_gt_idx_arr.reverse()
        print(left_gt_idx_arr)
        print(right_gt_idx_arr)

        max_size = 0
        for i in range(len(heights)):
            width = 1
            if left_gt_idx_arr[i] is not None:
                width += i - left_gt_idx_arr[i]
            if right_gt_idx_arr[i] is not None:
                width += right_gt_idx_arr[i] - i
            size = width * heights[i]
            # print(size)
            if size > max_size:
                max_size = size
        return max_size


sol = Solution()

data = [5,4,3,2,1]
r = sol.largestRectangleArea(data)
print(r)

# data = [1,2,3,4,5]
# r = sol.largestRectangleArea(data)
# print(r)

