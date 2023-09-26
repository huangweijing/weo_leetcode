from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        down_arr = [0] * len(maxHeights)
        up_arr = [0] * len(maxHeights)
        stk = []
        stk_sum = 0
        for i, height in enumerate(maxHeights):
            cnt = 1
            while len(stk) > 0 and stk[-1][0] >= height:
                item = stk.pop()
                stk_sum -= item[0] * item[1]
                cnt += item[1]
            stk.append([height, cnt])
            stk_sum += height * cnt
            up_arr[i] = stk_sum

        stk = []
        stk_sum = 0
        for j, height in enumerate(reversed(maxHeights)):
            i = len(maxHeights) - 1 - j
            cnt = 1
            while len(stk) > 0 and stk[-1][0] >= height:
                item = stk.pop()
                stk_sum -= item[0] * item[1]
                cnt += item[1]
            stk.append([height, cnt])
            stk_sum += height * cnt
            down_arr[i] = stk_sum

        ans = 0
        for i, height in enumerate(maxHeights):
            ans = max(ans, down_arr[i] + up_arr[i] - height)
        return ans

