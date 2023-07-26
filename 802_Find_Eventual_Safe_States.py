from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        to_g = [set[int]() for i in range(len(graph))]
        from_g = [set[int]() for i in range(len(graph))]
        is_safe_set = set[int]()
        safe_layer = set[int]()
        for i, adj_nodes in enumerate(graph):
            to_g[i] = set(adj_nodes)
            for adj in adj_nodes:
                from_g[adj].add(i)
            if len(to_g[i]) == 0:
                is_safe_set.add(i)
                safe_layer.add(i)

        while len(safe_layer) > 0:
            node = safe_layer.pop()
            prev_nodes = from_g[node]
            for prev in prev_nodes:
                to_g[prev].remove(node)
                if len(to_g[prev]) == 0:
                    is_safe_set.add(prev)
                    safe_layer.add(prev)

        ans = list(is_safe_set)
        ans.sort()
        return ans

data = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
r = Solution().eventualSafeNodes(data)
print(r)

