from typing import List
import math


class Solution:
    def average(self, salary: List[int]) -> float:
        min_val, max_val = math.inf, 0
        sum_val = 0
        for val in salary:
            min_val = min(val, min_val)
            max_val = max(val, max_val)
            sum_val += val
        avg = (sum_val - min_val - max_val) / (len(salary) - 2)
        return avg

data = [
    [4000,3000,1000,2000]
]
r = Solution().average(* data)
print(r)
