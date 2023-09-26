from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        try_bin = (1 << len(nums)) - 1
        nums_set = set(nums)
        n = len(nums)
        while n > 0:
            bin_str = bin(try_bin)[2:]
            if bin_str not in nums_set:
                return str.rjust(bin_str, n, "0")
            try_bin -= 1
        return ""
