from typing import List

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        arr = nums
        while len(arr) > 1:
            # print(arr)
            result = []
            for i in range(len(arr)):
                if i & 2 == 1:
                    continue
                if i % 4 == 0:
                    result.append(min(arr[i], arr[i + 1]))
                if i % 4 == 2:
                    result.append(max(arr[i], arr[i + 1]))
            arr = result
        return arr[0]

sol = Solution()
r = sol.minMaxGame([1,3,5,2,4,8,2,2])
print(r)
