class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums.copy())
        return nums
