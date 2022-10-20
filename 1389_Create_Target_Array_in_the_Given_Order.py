from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            idx = index[i]
            if idx == len(ans):
                ans.append(num)
            else:
                ans.insert(idx, num)
        return ans

data = [
      [0,1,2,3,4]
    , [0,1,2,2,1]
]
r = Solution().createTargetArray(* data)
print(r)
