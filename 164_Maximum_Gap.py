import heapq

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        heapq.heapify(nums)
        maximum_gap = 0
        last_num = heapq.heappop(nums)
        while len(nums) > 0:
            num = heapq.heappop(nums)
            gap = num - last_num
            if gap > maximum_gap:
                maximum_gap = gap
            last_num = num
        return maximum_gap

r = Solution().maximumGap([3,6,9,1])
print(r)