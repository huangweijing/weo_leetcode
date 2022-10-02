from typing import List
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort()
        idx = bisect.bisect_left(arr, x)
        left, right = idx-1, idx
        result = []
        while k != 0:
            if right >= len(arr):
                result.extend(arr[left - k + 1: left + 1])
                break
            if left < 0:
                result.extend(arr[right: right + k])
                break
            # print(arr[left], arr[right], abs(arr[left] - x), abs(arr[right] - x))
            if abs(arr[left] - x) <= abs(arr[right] - x):
                # print(arr[left])
                result.append(arr[left])
                left -= 1
                k -= 1
            else:
                # print(arr[right])
                result.append(arr[right])
                right += 1
                k -= 1
        result.sort()
        return result

data = [[1], 1, 5]
r = Solution().findClosestElements(* data)
print(r)