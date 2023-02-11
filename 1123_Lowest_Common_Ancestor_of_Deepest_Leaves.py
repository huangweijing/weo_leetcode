from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.parent = dict[TreeNode, TreeNode]()
        self.layer_node = dict[int, set[TreeNode]]()

    def calc_layer(self, parent: TreeNode, root: TreeNode, layer: int):
        if layer not in self.layer_node:
            self.layer_node[layer] = set[TreeNode]()
        self.layer_node[layer].add(root)
        self.parent[root] = parent
        if root.left is not None:
            self.calc_layer(root, root.left, layer + 1)
        if root.right is not None:
            self.calc_layer(root, root.right, layer + 1)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.calc_layer(None, root, 0)
        layer_list = list(self.layer_node.keys())
        layer_list.sort(reverse=True)
        leaves_set = self.layer_node[layer_list[0]]
        common_list = deque()
        common_set = set[TreeNode]()
        for leave in leaves_set:
            node = leave
            parent_list = deque()
            while node is not None:
                parent_list.append(node)
                node = self.parent[node]
            if len(common_list) == 0:
                common_list = parent_list
                common_set = set(common_list)
            else:
                for p in parent_list:
                    if p in common_set:
                        while common_list[0] != p:
                            to_remove = common_list.popleft()
                            common_set.remove(to_remove)
                        break
        return common_list[0]

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
t = make_leetree([1,25,2,null,49,18,3,112,59,33,29,4,5,null,128,125,153,75,43,null,38,7,8,34,6,196,null,null,180,null,295,237,96,53,55,51,40,10,135,11,12,56,199,9,47,253,null,209,null,null,null,null,286,null,null,159,230,113,200,71,52,85,63,124,21,null,145,15,19,14,16,78,225,null,null,13,41,62,103,265,null,261,256,null,null,null,null,263,null,175,168,null,null,193,118,null,229,null,null,77,74,192,null,23,70,299,null,20,87,31,22,28,17,156,208,null,102,null,null,80,50,null,65,null,221,122,201,null,null,null,null,null,null,null,277,250,198,240,null,null,null,141,137,null,null,129,114,109,143,null,null,30,24,291,79,null,null,121,null,97,null,178,null,26,null,32,null,39,37,null,172,null,null,212,null,null,146,null,60,86,null,null,null,null,null,null,null,null,null,null,null,202,null,null,289,169,235,163,null,null,292,null,213,null,173,152,160,67,76,44,27,null,null,81,206,null,272,132,null,null,271,69,35,66,null,64,null,null,127,null,248,null,null,188,186,68,95,166,null,219,null,null,null,null,226,null,null,177,181,null,null,null,null,194,218,158,null,231,184,83,null,null,110,73,null,36,72,89,131,223,null,null,null,210,164,null,null,null,84,45,167,157,106,138,148,161,null,298,null,null,null,null,189,93,null,115,98,null,null,null,279,269,null,null,null,183,null,null,220,null,null,null,null,null,null,null,null,185,null,222,264,null,136,42,57,null,130,195,null,null,null,234,null,262,null,null,null,116,88,54,46,null,null,182,null,242,187,null,null,null,300,null,170,null,null,null,251,133,174,120,241,null,139,null,null,null,null,null,null,null,null,null,244,null,null,null,null,245,null,48,90,144,257,259,233,null,null,null,null,null,282,254,134,101,91,147,117,228,58,null,255,null,null,null,null,null,null,null,null,null,null,null,142,null,null,null,null,null,null,null,null,null,274,null,273,82,126,94,92,215,246,null,null,null,275,null,null,null,null,null,null,null,179,123,null,100,99,290,null,null,205,null,null,61,247,null,null,null,151,276,null,null,null,154,105,150,149,140,104,null,155,null,null,null,266,null,null,null,191,214,null,297,null,107,108,null,null,null,249,278,238,null,252,260,null,null,null,165,null,243,null,null,216,293,288,null,217,224,null,null,176,null,null,203,227,236,null,null,null,162,111,232,171,null,null,null,null,null,null,null,null,null,null,190,197,null,270,null,null,294,null,null,null,284,null,null,267,null,268,211,207,null,null,null,null,null,null,119,null,239,283,285,280,null,null,258,281,null,null,null,null,null,null,null,null,null,null,null,296,287,null,null,204])
r = Solution().lcaDeepestLeaves(t)
print(r.val)
