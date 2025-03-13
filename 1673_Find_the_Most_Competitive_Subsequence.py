from typing import List
import heapq


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        idx = 0
        heap = []
        left = 0
        ans = []
        for i in range(k):
            while idx <= len(nums) - k + i:
                heapq.heappush(heap, [nums[idx], idx])
                idx += 1
            while len(heap) > 0:
                item = heapq.heappop(heap)
                # print(f"item={item}")
                if item[1] < left:
                    pass
                else:
                    ans.append(item[0])
                    left = item[1]
                    break
        return ans
    

data = [
    [2,4,3,3,5,4,9,6]
    , 4
]
r = Solution().mostCompetitive(*data)
print(r)

        