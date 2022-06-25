from typing import List
import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        target_heap = list(map(lambda x: -x, target))
        heapq.heapify(target_heap)
        target_sum = -sum(target_heap)
        while True:
            target_max = - heapq.heappop(target_heap)
            # print(target_heap, target_max, target_sum)
            if target_sum == len(target) and target_max == 1:
                return True

            if target_sum - target_max == 1:
                target_max_last = 1
            else:
                if target_sum != target_max and target_max / (target_sum - target_max) > 2:
                    target_max_last = target_max % (target_sum - target_max)
                else:
                    target_max_last = target_max - (target_sum - target_max)

            if target_max_last < 1:
                return False

            heapq.heappush(target_heap, -target_max_last)
            target_sum = target_sum - (target_max - target_max_last)

data = [2]
r = Solution().isPossible(data)
print(r)
