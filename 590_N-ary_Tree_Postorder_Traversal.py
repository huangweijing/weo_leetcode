class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = list[int]()
        if root is None:
            return result
        if root.children is not None:
            for node in root.children:
                node_result = self.preorder(node)
                result.extend(node_result)
        result.append(root.val)
        return result