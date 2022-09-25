from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        result = []
        for i in range(n):
            left, right = l[i], r[i]
            arr = nums[left: right + 1]
            arr.sort()
            step = int((arr[-1] - arr[0]) / (right - left))
            okay = True
            for t in range(1, len(arr)):
                if arr[t] - arr[t - 1] != step:
                    okay = False
                    break
            result.append(okay)
        return result

data = [[4,6,5,9,3,7]
        , [0,0,2]
        , [2,3,5]]
r = Solution().checkArithmeticSubarrays(* data)
print(r)
