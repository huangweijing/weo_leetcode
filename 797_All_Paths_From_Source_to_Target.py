from typing import List
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        node_queue = deque([[0]])
        result = []
        while len(node_queue) > 0:
            path = node_queue.popleft()
            next_nodes = graph[path[-1]]
            for next_node in next_nodes:
                new_path = path.copy()
                new_path.append(next_node)
                if next_node == len(graph) - 1:
                    result.append(new_path)
                else:
                    node_queue.append(new_path)
        return result

data_graph = [[1,2],[3],[3],[]]
r = Solution().allPathsSourceTarget(data_graph)
print(r)

