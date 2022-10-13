from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        from_node = [[] for _ in range(n)]
        for edge in edges:
            from_node[edge[1]].append(edge[0])
        result = []
        for i, node in enumerate(from_node):
            if len(node) == 0:
                result.append(i)
        return result

data = [
5
, [[0,1],[2,1],[3,1],[1,4],[2,4]]
]
r = Solution().findSmallestSetOfVertices(* data)
print(r)

