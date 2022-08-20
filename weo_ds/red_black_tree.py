import tree_tools

class TreeNode:
    def __init__(self):
        self.key = None
        self.val = None
        self.left = None
        self.right = None
        self.color = False # True: red, False: black

class RBTree:

    def __init__(self):
        self.root = None
        self.node_count = 0

    def add(self, key, value):
        self.root = self.put(self.root, key, value)

    def put(self, node: TreeNode, key: int, value: int) -> TreeNode:
        if node is None:
            new_node = TreeNode()
            new_node.color = True
            new_node.val = value
            return new_node
        if value < node.val:
            node.left = self.put(node.left, key, value)
        elif value > node.val:
            node.right = self.put(node.right, key, value)
        else:
            node.val = value

        node_color = node.color
        if not self.is_red(node.left) and self.is_red(node.right):
            node.right.color = False
            node = self.rotate_left(node)
            node.left.color = True
            node.color = node_color
        if self.is_red(node.left) and self.is_red(node.left.left):
            # if node.left is None, is_red(node.left) would be False, and the later half won't be executed
            node = self.rotate_right(node)
            node.right.color = True
            node.color = node_color
        if self.is_red(node.left) and self.is_red(node.right):
            node.left.color = False
            node.right.color = False
            node.color = True
        return node

    def is_red(self, node: TreeNode):
        if node is None:
            return False
        return node.color

    def rotate_left(self, node) -> TreeNode:
        if node.right is None:
            return
        right_node = node.right
        right_left_tree = node.right.left
        right_node.left = node
        node.right = right_left_tree
        return right_node

    def rotate_right(self, node) -> TreeNode:
        if node.left is None:
            return
        left_node = node.left
        left_right_tree = node.left.right
        left_node.right = node
        node.left = left_right_tree
        return left_node

data = [3, 8, 9, 2, 4, 11, 1]
t = RBTree()
for d in data:
    t.add(d, d)
    print(tree_tools.preorder_encode(t.root))

# t.root = t.rotate_left(t.root)
# print(tree_tools.preorder_encode(t.root))
# t.root = t.rotate_right(t.root)
# print(tree_tools.preorder_encode(t.root))

        # if self.root is None:
        #     self.root = TreeNode()
        #     self.root.val = value
        #     return
