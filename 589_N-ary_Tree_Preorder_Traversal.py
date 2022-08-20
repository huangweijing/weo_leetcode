class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = list[int]()
        if root is None:
            return result
        result.append(root.val)
        if root.children is not None:
            for node in root.children:
                node_result = self.preorder(node)
                result.extend(node_result)
        return result
