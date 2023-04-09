class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        ans = sum(map(lambda x: max_num - x, nums))
        return ans