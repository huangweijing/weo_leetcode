from sortedcontainers import SortedList

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sl_arr = [SortedList() for _ in range(10)]
        for num in nums:
            sl_arr[int(max(str(num)))].add(num)
        ans = -1
        for sl in sl_arr:
            if len(sl) >= 2:
                ans = max(ans, sl[-1] + sl[-2])
        return ans