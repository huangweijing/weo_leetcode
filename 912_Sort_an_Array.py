from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []
        arr = [0] * (10 ** 5 + 1)
        max_num = 0
        for num in nums:
            num += 5 * (10 ** 4)
            arr[num] += 1
            max_num = max(max_num, num)
        for i in range(max_num + 1):
            if arr[i] == 0:
                continue
            num = i - 5 * (10 ** 4)
            ans.extend([num for _ in range(arr[i])])
        return ans

nums = [5,1,1,2,0,0]
r = Solution().sortArray(nums)
print(r)
