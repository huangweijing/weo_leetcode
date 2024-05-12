from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = list(zip(quality, wage))
        workers.sort(key=lambda x: x[1] / x[0])
        ratio = workers[k - 1][1] / workers[k - 1][0]
        quality_heap = [-w[0] for w in workers[: k]]
        # print(workers, quality_heap, ratio)
        sum_quality = -sum(quality_heap)
        heapq.heapify(quality_heap)
        ans = sum_quality * ratio
        for i in range(k, len(workers)):
            worker = workers[i]
            # print(sum_quality, quality_heap, worker)
            # if (sum_quality + quality_heap[0] + worker[0]) * (worker[1] / worker[0]) < ans:
            sum_quality = sum_quality + quality_heap[0] + worker[0]
            heapq.heappop(quality_heap)
            heapq.heappush(quality_heap, -worker[0])
            ratio = worker[1] / worker[0]
            ans = min(ans, sum_quality * ratio)
            # print(sum_quality, quality_heap, worker)
            # print("---")

        return ans



data = [
    [32, 43, 66, 9, 94, 57, 25, 44, 99, 19]
    , [187, 366, 117, 363, 121, 494, 348, 382, 385, 262]
    , 4
]
r = Solution().mincostToHireWorkers(*data)
print(r)



