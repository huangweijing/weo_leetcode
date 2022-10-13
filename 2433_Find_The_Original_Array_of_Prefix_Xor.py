from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = []
        xor_sum = 0
        for num in pref:
            pre = xor_sum ^ num
            result.append(pre)
            xor_sum = xor_sum ^ pre
        return result

r = Solution().findArray([13])
print(r)
