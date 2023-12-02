from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        val, min_val, max_val = 0, 0, 0
        for diff in differences:
            val = val + diff
            min_val = min(min_val, val)
            max_val = max(max_val, val)
        return max(0, upper - lower - (max_val - min_val) + 1)


data = [
    [4,-7,2]
    , 3
    , 6]
r = Solution().numberOfArrays(*data)
print(r)