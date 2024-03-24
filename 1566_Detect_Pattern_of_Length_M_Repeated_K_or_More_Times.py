from typing import List
from collections import Counter

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m * k > len(arr):
            return False
        for i in range(len(arr)):
            if i + m * k > len(arr):
                break
            okay = True
            for j in range(1, k):
                for idx in range(m):
                    if arr[i + idx + j * m] != arr[i + idx]:
                        okay = False
                        break
                if not okay:
                    break
            if okay:
                return True
        return False




r = Solution().containsPattern([1,2,1,2,1,2], 2, 3)
print(r)


