from sortedcontainers import SortedList


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        sl = SortedList()
        sum_len = 0
        ans = []
        for query in queries:
            idx = sl.bisect_left([query[0], 0])
            if idx < len(sl) and sl[idx][0] == query[0] and sl[idx][1] > query[1]:
                pass
            elif 0 < idx and sl[idx - 1][1] >= query[1]:
                pass
            else:
                while len(sl) > idx and sl[idx][1] <= query[1]:
                    sum_len -= sl[idx][1] - sl[idx][0] - 1
                    sl.pop(idx)
                if idx == 0 or sl[idx - 1][1] <= query[1]:
                    sl.add(query)
                    sum_len += query[1] - query[0] - 1
            # print(sl, n, sum_len)
            ans.append(n - 1 - sum_len)
        return ans