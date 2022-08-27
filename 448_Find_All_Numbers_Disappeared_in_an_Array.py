class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [False] * (len(nums) + 1)
        for num in nums:
            arr[num] = True
        result = list[int]()
        for i in range(1, len(nums) + 1):
            if not arr[i]:
                result.append(i)
        return result