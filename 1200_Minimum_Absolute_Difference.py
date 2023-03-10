from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_diff = math.inf
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                ans = []
            if diff == min_diff:
                ans.append([arr[i - 1], arr[i]])
        return ans
