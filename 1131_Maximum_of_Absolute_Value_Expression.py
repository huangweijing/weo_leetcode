from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = -10e9
        max_val = [-10e9] * 4
        for i in range(len(arr1)):
            v = [
                arr1[i] + arr2[i] + max_val[3] + i
                , -arr1[i] + arr2[i] + max_val[2] + i
                , arr1[i] - arr2[i] + max_val[1] + i
                , -arr1[i] - arr2[i] + max_val[0] + i]
            ans = max(ans, max(v))
            max_val[0] = max(max_val[0], arr1[i] + arr2[i] - i)
            max_val[1] = max(max_val[1], -arr1[i] + arr2[i] - i)
            max_val[2] = max(max_val[2], arr1[i] - arr2[i] - i)
            max_val[3] = max(max_val[3], -arr1[i] - arr2[i] - i)
        return ans
    

data = [
    [1,-2,-5,0,10]
    , [0,-2,-1,-7,-4]
]
r = Solution().maxAbsValExpr(*data)
print(r)
            