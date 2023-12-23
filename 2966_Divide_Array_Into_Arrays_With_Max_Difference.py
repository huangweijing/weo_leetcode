from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        arr = []
        for i, num in enumerate(nums):
            if i % 3 == 0:
                arr.append([num])
            else:
                if num - arr[-1][0] <= k:
                    arr[-1].append(num)
                else:
                    return []
        return arr


data = [
    [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2]
    , 2
]
r = Solution().divideArray(*data)
print(r)