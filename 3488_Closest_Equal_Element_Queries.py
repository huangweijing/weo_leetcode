from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prev_idx_arr = [-1] * len(nums)
        next_idx_arr = [-1] * len(nums)
        last_idx, first_idx = dict[int, int](), dict[int, int]()
        val_idx = dict[int, int]()
        for i, num in enumerate(nums):
            if num not in first_idx:
                first_idx[num] = i
            if num not in last_idx:
                last_idx[num] = i
            else:
                last_idx[num] = max(i, last_idx[num])
        # print(first_idx, last_idx)
        for i, num in enumerate(nums):
            if num in val_idx:
                prev_idx_arr[i] = val_idx[num]
            else:
                if i != last_idx[num]:
                    prev_idx_arr[i] = last_idx[num]
            val_idx[num] = i
        val_idx.clear()
        for i, num in enumerate(reversed(nums)):
            i = len(nums) - 1 - i
            if num in val_idx:
                next_idx_arr[i] = val_idx[num]
            else:
                if i != first_idx[num]:
                    next_idx_arr[i] = first_idx[num]
            val_idx[num] = i
        # print(prev_idx_arr, next_idx_arr)
        ans = []
        for query in queries:
            if next_idx_arr[query] == -1:
                ans.append(-1)
            else:
                ans.append(min(
                    abs(next_idx_arr[query] - query + len(nums)) % len(nums)
                    , abs(next_idx_arr[query] - query) % len(nums)
                    , abs(query - prev_idx_arr[query] + len(nums)) % len(nums)
                    , abs(query - prev_idx_arr[query]) % len(nums)
                ))
        return ans
    

data = [
    [6,12,17,9,16,7,6]
    , [5,6,0,4]
]
r = Solution().solveQueries(*data)
print(r)