from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        org_arr = arr.copy()
        org_arr.sort()
        sorted_idx = len(arr)
        ans = []
        while sorted_idx > 0:
            max_num = org_arr.pop()
            # print(max_num, arr)
            idx = arr[:sorted_idx].index(max_num)
            # print(idx, arr[:idx + 1][::-1], arr[:idx + 1])
            ans.append(idx + 1)
            arr[:idx + 1] = arr[:idx + 1][::-1]
            ans.append(sorted_idx)
            arr[:sorted_idx] = arr[:sorted_idx][::-1]
            # print(arr, sorted_idx)
            sorted_idx = sorted_idx - 1
        return ans

data = [3,2,4,1]
print(data)
r = Solution().pancakeSort(data)
print(r)

