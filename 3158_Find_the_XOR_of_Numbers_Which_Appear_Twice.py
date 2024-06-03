from collections import Counter


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for v, c in cnt.items():
            if c == 2:
                ans ^= v
        return ans

