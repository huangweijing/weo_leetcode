import bisect
from typing import List
from collections import Counter
from bisect import bisect_left

class Solution:
    def countServers(self, n: int, logs: List[List[int]]
                     , x: int, queries: List[int]) -> List[int]:
        # logs.sort(key=lambda e: e[1])
        server_cnt = Counter()
        server_log_arr = []
        for log in logs:
            server_log_arr.append([log[0], log[1] - x])
            server_log_arr.append([-log[0], log[1] + 1])
        server_log_arr.sort(key=lambda e: e[1])
        time_arr = []
        server_cnt_arr = []
        for server_log in server_log_arr:
            time = server_log[1]
            if server_log[0] > 0:
                server_cnt[server_log[0]] += 1
            if server_log[0] < 0:
                server_cnt[-server_log[0]] -= 1
                if server_cnt[-server_log[0]] == 0:
                    del server_cnt[-server_log[0]]
            time_arr.append(time)
            server_cnt_arr.append(len(server_cnt))
        # print(time_arr)
        # print(server_cnt_arr)
        ans = []
        for query in queries:
            idx = bisect.bisect_right(time_arr, query - x) - 1
            # if time_arr[idx] > query - x:
            #     idx -= 1
            # print(query - 5, idx)
            ans.append(n - server_cnt_arr[idx])
        return ans

data = [
    3
    , [[2, 4], [2, 1], [1, 2], [3, 1]]
    , 2
    , [3, 4]
]
r = Solution().countServers(* data)
print(r)

