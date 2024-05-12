from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(reverse=True, key=lambda x: [len(x), x])
        return nums[k - 1]
