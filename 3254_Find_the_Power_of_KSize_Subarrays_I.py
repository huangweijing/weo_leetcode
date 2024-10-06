from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        diff_arr = []
        for i, num in enumerate(nums[1:], start=1):
            if nums[i] == nums[i - 1] + 1:
                diff_arr.append(0)
            else:
                diff_arr.append(1)
        ans = []
        sum_ascending = sum(diff_arr[: k - 1])
        if sum_ascending == 0:
            ans.append(nums[k - 1])
        else:
            ans.append(-1)
        for i in range(k, len(nums)):
            sum_ascending -= diff_arr[i - k]
            sum_ascending += diff_arr[i - 1]
            if sum_ascending == 0:
                ans.append(nums[i])
            else:
                ans.append(-1)
        return ans


data = [
[1,2,3,4,3,2,5]
, 3
]
r = Solution().resultsArray(*data)
print(r)


