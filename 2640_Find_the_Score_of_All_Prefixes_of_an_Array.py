from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []
        max_val = 0
        for num in nums:
            max_val = max(max_val, num)
            conversion_val = num + max_val
            if len(ans) > 0:
                ans.append(ans[-1] + conversion_val)
            else:
                ans.append(conversion_val)
        return ans


