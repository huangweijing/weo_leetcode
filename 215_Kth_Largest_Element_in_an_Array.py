from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # num_set = set[int]()
        # for num in nums:
        #     num_set.add(num)
        # num_list = list(num_set)
        # num_list.sort(reverse=True)
        # return num_list[k - 1]
        nums.sort(reverse=True)
        return nums[k - 1]

print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))