from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt_arr1 = Counter(arr1)
        ans = []
        for num in arr2:
            if num in cnt_arr1:
                ans.extend([num] * cnt_arr1[num])
            del cnt_arr1[num]
        tail = sorted([key for key in cnt_arr1])
        for num in tail:
            ans.extend([num] * cnt_arr1[num])
        return ans

        
