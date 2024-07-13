from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        num_list = list(zip(nums1, nums2))
        num_list.sort(key=lambda x: x[1])
        heap = []
        heap_sum = 0
        heap_min = num_list[-1][1]
        for i in range(k):
            arr = num_list.pop()
            heap_sum += arr[0]
            heapq.heappush(heap, arr[0])
            heap_min = arr[1]
        ans = heap_min * heap_sum
        while len(num_list) > 0:
            arr = num_list.pop()
            heap_sum -= heapq.heappop(heap)
            heap_sum += arr[0]
            heapq.heappush(heap, arr[0])
            heap_min = arr[1]
            ans = max(ans, heap_sum * heap_min)
        return ans




data = [
    [2, 1, 14, 12]
    , [11, 7, 13, 6]
    , 3
]
r = Solution().maxScore(* data)
print(r)

