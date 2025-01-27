from typing import List
from collections import defaultdict


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        g = defaultdict(lambda: set[int]())
        for i in range(n - 1):
            g[i].add(i + 1)
        for query in queries:
            g[query[0]].add(query[1])
            cur = set[int]([0])
            visited = set[int]()
            dist = 0
            while len(cur) > 0:
                if n - 1 in visited:
                    ans.append(dist)
                    break
                new_cur = set[int]()
                while len(cur) > 0:
                    node = cur.pop()
                    for adj in g[node]:
                        if adj not in visited:
                            visited.add(adj)
                            new_cur.add(adj)
                dist += 1
                cur = new_cur
        return ans
                
data = [
5
, [[1,4],[2,4]]
]
r = Solution().shortestDistanceAfterQueries(*data)
print(r)