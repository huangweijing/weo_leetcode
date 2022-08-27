from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.connection = dict[int, set[int]]()

    def gen_graph(self, root: Optional[TreeNode]):
        if root.val not in self.connection:
            self.connection[root.val] = set[int]()
        if root.left is not None:
            self.connection[root.val].add(root.left.val)
            if root.left.val not in self.connection:
                self.connection[root.left.val] = set[int]()
            self.connection[root.left.val].add(root.val)
            self.gen_graph(root.left)

        if root.right is not None:
            self.connection[root.val].add(root.right.val)
            if root.right.val not in self.connection:
                self.connection[root.right.val] = set[int]()
            self.connection[root.right.val].add(root.val)
            self.gen_graph(root.right)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.gen_graph(root)
        infected = [False] * (10 ** 5 + 1)
        infected[start] = True
        infected_size = 1
        q = deque()
        q.append(start)
        result = 0
        while len(q) > 0:
            result += 1
            new_q = deque()
            while len(q) > 0:
                node = q.popleft()
                adj_node_set = self.connection[node]
                for adj_node in adj_node_set:
                    if infected[adj_node]:
                        continue
                    infected[adj_node] = True
                    # print(str(adj_node) + " affected in time " + str(result))
                    new_q.append(adj_node)
            q = new_q
        return result - 1

def make_leetree(data_list: list[int]) -> TreeNode:
    idx = 0
    root = TreeNode(data_list[idx])
    idx += 1
    node_queue = deque[TreeNode]()
    node_queue.append(root)
    while len(node_queue) > 0 and idx < len(data_list):
        node = node_queue.popleft()
        if data_list[idx] is not None:
            node.left = TreeNode(data_list[idx])
            node_queue.append(node.left)
        else:
            node.left = None
        idx += 1
        if idx == len(data_list):
            break
        if data_list[idx] is not None:
            node.right = TreeNode(data_list[idx])
            node_queue.append(node.right)
        else:
            node.right = None
        idx += 1
    return root

null = None
data = make_leetree([1,5,3,null,4,10,6,9,2])
r = Solution().amountOfTime(data, 1)
print(r)