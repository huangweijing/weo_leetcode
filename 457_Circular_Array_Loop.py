from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            visited = set[int]()
            cur1, cur2 = i, i
            pos = nums[cur1] > 0
            while cur1 not in visited and nums[cur1] > 0 == pos:
                visited.add(cur1)
                cur1 = (cur1 + nums[cur1] + len(nums)) % len(nums)
                cur2 = (cur2 + nums[cur2] + len(nums)) % len(nums)
                cur2 = (cur2 + nums[cur2] + len(nums)) % len(nums)
                if cur1 == cur2:
                    return True
        return False
    
data = [2,-1,1,2,2]
r = Solution().circularArrayLoop(data)
print(r)
        