from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set(nums)
        for e in s.copy():
            s.add(int(str(e)[::-1]))
        return len(s)
