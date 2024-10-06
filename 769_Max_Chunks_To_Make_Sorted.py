from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        idx = 0
        while idx < len(arr):
            ans += 1
            min_val, max_val = arr[idx], arr[idx]
            start = idx
            while idx < len(arr) and not (min_val == start and max_val == min_val + idx - start):
                idx += 1
                if idx >= len(arr):
                    break
                min_val = min(arr[idx], min_val)
                max_val = max(arr[idx], max_val)
            idx += 1
        return ans
    
data = [1,0,2,3,4]
r = Solution().maxChunksToSorted(data)
print(r)