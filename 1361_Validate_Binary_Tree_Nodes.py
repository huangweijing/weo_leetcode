from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent_node = dict[int, int]()
        for i, node in enumerate(leftChild):
            if node == -1:
                continue
            if node in parent_node:
                return False
            parent_node[node] = i
        for i, node in enumerate(rightChild):
            if node == -1:
                continue
            if node in parent_node:
                return False
            parent_node[node] = i
        root = 0
        visited = set[int]([root])
        while root in parent_node:
            root = parent_node[root]
            if root in visited:
                return False
            visited.add(root)
        visited = set[int]([root])
        stk = [root]
        while len(stk) > 0:
            # print(stk)
            node = stk.pop()
            if leftChild[node] != -1:
                if leftChild[node] in visited:
                    return False
                stk.append(leftChild[node])
                visited.add(leftChild[node])
            if rightChild[node] != -1:
                if rightChild[node] in visited:
                    return False
                stk.append(rightChild[node])
                visited.add(rightChild[node])
        return len(visited) == n


data = [
4
, [1,-1,3,-1]
, [2,-1,-1,-1]
]
r = Solution().validateBinaryTreeNodes(* data)
print(r)