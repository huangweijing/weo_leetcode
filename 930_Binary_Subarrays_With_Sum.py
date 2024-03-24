from typing import List
from collections import Counter



class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = 0
        cnt_dict = Counter()
        cnt_dict[0] = 1
        ans = 0
        for num in nums:
            cnt += 1 if num == 1 else 0
            if cnt >= goal:
                ans += cnt_dict[cnt - goal]
            cnt_dict[cnt] += 1
        return ans

data = [
    [1,0,1,0,1]
    , 0
]
r = Solution().numSubarraysWithSum(* data)
print(r)
