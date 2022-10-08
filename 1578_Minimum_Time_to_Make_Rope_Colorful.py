from typing import List
import  math

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        color_len = 0
        sum_color = 0
        max_cost = -math.inf
        result = 0

        for i, color in enumerate(colors):
            max_cost = max(neededTime[i], max_cost)
            sum_color += neededTime[i]
            color_len += 1
            if i + 1 == len(colors) or colors[i + 1] != color:
                # print(color, sum_color, max_cost)
                result += sum_color - max_cost
                color_len = 0
                max_cost = -math.inf
                sum_color = 0

        return result

data_colors = "aabaa"
data_neededTime = [1,2,3,4,1]
r = Solution().minCost(data_colors, data_neededTime)
print(r)

