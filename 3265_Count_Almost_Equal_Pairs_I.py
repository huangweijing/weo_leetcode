from typing import List
from collections import  Counter


class Solution:
    def is_diff(self, s1: str, s2: str) -> bool:
        s1 = s1.rjust(max(len(s1), len(s2)), "0")
        s2 = s2.rjust(max(len(s1), len(s2)), "0")
        if Counter(s1) != Counter(s2):
            return True
        cnt = 0
        for i in range(len(s1)):
            ch1, ch2 = s1[i], s2[i]
            if ch1 != ch2:
                cnt += 1
            if cnt > 2:
                return True
        if cnt in (0, 2):
            return False
        return True

    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        for i, n1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                n2 = nums[j]
                if not self.is_diff(str(n1), str(n2)):
                    # print(n1, n2)
                    ans += 1
        return ans


data = [8,12,5,5,14,3,12,3,3,6,8,20,14,3,8]
r = Solution().countPairs(data)
print(r)