from typing import List
import math

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        min_result = math.inf
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                mul = arr[i] * arr[j]
                new_arr = arr.copy()
                del new_arr[i]
                del new_arr[j - 1]
                new_arr.append(mul)
                result = mul + self.mctFromLeafValues(new_arr)
                min_result = min(min_result, result)
        print(arr, min_result)
        return min_result

data_arr = [6,2,4]
r = Solution().mctFromLeafValues(data_arr)
print(r)