"""
# Definition for a Node.
"""
from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        create_graph_dict = dict[int, Node]()
        visited = set[int]()
        q = deque()
        q.append(node)
        visited.add(node.val)
        while len(q) > 0:
            n = q.popleft()
            if n.val not in create_graph_dict:
                create_graph_dict[n.val] = Node(n.val)
            for nei in n.neighbors:
                if nei.val not in create_graph_dict:
                    create_graph_dict[nei.val] = Node(nei.val)
                create_graph_dict[n.val].neighbors.append(create_graph_dict[nei.val])
                if nei.val in visited:
                    continue
                q.append(nei)
                visited.add(nei.val)
        return create_graph_dict[node.val]






