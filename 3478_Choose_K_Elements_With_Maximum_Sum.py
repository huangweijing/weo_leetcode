from typing import List
import heapq

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        heap = []
        new_nums1 = list(sorted(enumerate(nums1), key=lambda x: [x[1], x[0]]))
        sum_val = 0
        ans = []
        less_than_idx = 0
        for i, val in new_nums1:
            while new_nums1[less_than_idx][1] < val:
                heapq.heappush(heap, nums2[new_nums1[less_than_idx][0]])
                sum_val += nums2[new_nums1[less_than_idx][0]]
                while len(heap) > k:
                    popped_val = heapq.heappop(heap)
                    sum_val -= popped_val
                less_than_idx += 1
            ans.append([sum_val, i])
        ans.sort(key=lambda x: x[1])
        return [val[0] for val in ans]
    
data = [
    [4,2,1,5,3]
    , [10,20,30,40,50]
    , 2
]
r = Solution().findMaxSum(*data)
print(r)
        