from typing import List
import math


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -math.inf
        for i in range(k):
            end = len(energy) - 1 - i
            sum_energy = 0
            jump_cnt = 0
            while end - jump_cnt * k >= 0:
                sum_energy += energy[end - jump_cnt * k]
                ans = max(ans, sum_energy)
                jump_cnt += 1
        return ans


data = [
    [5,-10,4,3,5,-9,9,-7]
    , 2
]
r = Solution().maximumEnergy(* data)
print(r)