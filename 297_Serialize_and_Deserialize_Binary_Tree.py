from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root) -> str:
        encoded_list = self.preorder_encode(root)
        return ",".join(encoded_list)

    def deserialize(self, data) -> TreeNode:
        arr = data.split(",")
        if len(arr) == 0:
            return None
        return self.build_tree(arr, [0])

    def preorder_encode(self, root: TreeNode) -> list[str]:
        if root is None:
            return ["None"]
        result = list[str]()
        result.append(str(root.val))
        result.extend(self.preorder_encode(root.left))
        result.extend(self.preorder_encode(root.right))
        return result

    def build_tree(self, preorder: list[str], idx: list[int]) -> Optional[TreeNode]:
        if idx[0] >= len(preorder):
            return None
        root_val = preorder[idx[0]]
        idx[0] += 1
        if root_val == "None":
            return None
        root = TreeNode(root_val)
        root.left = self.build_tree(preorder, idx)
        root.right = self.build_tree(preorder, idx)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

codec = Codec()
root = codec.deserialize(",".join(["1", "None", "2", "None", "None"]))
encoded = codec.serialize(root)
print(encoded)
# tree = codec.deserialize(",".join(['3', '2', '3', '4', '3', '2', '3', '4']))
# print(tree.left.val)


print(root.right.left)