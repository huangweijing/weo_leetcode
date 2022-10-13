from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        result = []
        arr_len = len(arr)
        for n in arr:
            if n == 0:
                result.extend([0, 0])
            else:
                result.append(n)
        arr.clear()
        arr.extend(result[:arr_len])
