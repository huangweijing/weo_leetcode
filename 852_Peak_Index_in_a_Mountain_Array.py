from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 1
        mid = right >> 1
        while left <= right:
            # print(left, right)
            # print(f"mid={mid}, res_mid={res_mid}, res_mid_m1={res_mid_m1}, {left}, {right}")
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid + 1] > arr[mid] > arr[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
            # print(left, right)
            mid = left + right >> 1
        return mid

data = [0,2,3,0]
r = Solution().peakIndexInMountainArray(data)
print(r)