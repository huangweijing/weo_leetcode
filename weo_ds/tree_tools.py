class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
        self.color = False # True: red, False: black

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

def print_tree(root_node: TreeNode, print_list: list[int]):
    node_queue: deque[TreeNode] = deque[TreeNode]()
    node_queue.append(root_node)
    while len(node_queue) != 0:
        node = node_queue.popleft()
        if node is None:
            print_list.append(None)
            continue
        print_list.append(node.val)
        node_queue.append(node.left)
        node_queue.append(node.right)
    print(print_list)



def preorder_encode(root: TreeNode) -> list[str]:
    if root is None:
        return ["None"]
    result = list[str]()
    result.append(str(root.val))
    result.extend(preorder_encode(root.left))
    result.extend(preorder_encode(root.right))
    return result

def build_tree(preorder: list[str], idx: list[int]) -> TreeNode:
    if idx[0] >= len(preorder):
        return None
    root_val = preorder[idx[0]]
    idx[0] += 1
    if root_val == "None":
        return None
    root = TreeNode(root_val)
    root.left = build_tree(preorder, idx)
    root.right = build_tree(preorder, idx)
    return root