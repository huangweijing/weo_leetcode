from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        ans = 0
        for time in processorTime:
            for i in range(4):
                task_time = tasks.pop()
                ans = max(ans, time + task_time)
                print(time, task_time)
        return ans

data = [
    [121,99]
    , [287,315,293,260,333,362,69,233]
]

r = Solution().minProcessingTime(*data)
print(r)