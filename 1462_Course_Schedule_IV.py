from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_map = [set[int]() for _ in range(numCourses)]
        post_map = [set[int]() for _ in range(numCourses)]
        for req in prerequisites:
            pre_map[req[0]].add(req[1])
            post_map[req[1]].add(req[0])
        ans = []
        for query in queries:
            next = set[int]([query[0]])
            visited = set[int]()
            found = False
            while len(next) > 0:
                new_next = set[int]()
                while len(next) > 0:
                    node = next.pop()
                    visited.add(node)
                    for adj in pre_map[node]:
                        if adj not in visited:
                            new_next.add(adj)
                next = new_next
                if query[1] in next:
                    found = True
                    break
            ans.append(found)
        return ans
    

data = [
3
, [[1,2],[1,0],[2,0]]
, [[1,0],[1,2]]
]
r = Solution().checkIfPrerequisite(*data)
print(r)
            



