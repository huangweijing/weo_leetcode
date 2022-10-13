from typing import List
from collections import Counter

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = logs[0][1]
        max_id = logs[0][0]
        for i in range(1, len(logs)):
            time = logs[i][1] - logs[i - 1][1]
            # print(logs[i][1], logs[i - 1][1], time)
            if time > max_time:
                max_time = time
                max_id = logs[i][0]
            if time == max_time:
                if logs[i][0] < max_id:
                    max_id = logs[i][0]
        return max_id

r = Solution().hardestWorker(26, [[1,1],[3,7],[2,12],[7,17]])
print(r)


