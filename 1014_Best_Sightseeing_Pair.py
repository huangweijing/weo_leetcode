from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        value_plus_pos, value_minus_pos = [], []
        for i, val in enumerate(values):
            value_plus_pos.append(val + i)
            value_minus_pos.append(val - i)

        max_value_minus_pos_from_tail = [0] * len(values)
        sum_tail = -math.inf
        for i in range(len(value_minus_pos) - 1, -1, -1):
            max_value_minus_pos_from_tail[i] = sum_tail
            sum_tail = max(value_minus_pos[i], sum_tail)
        ans = -math.inf
        for i in range(len(values)):
            ans = max(ans, max_value_minus_pos_from_tail[i] + value_plus_pos[i])
        return ans

