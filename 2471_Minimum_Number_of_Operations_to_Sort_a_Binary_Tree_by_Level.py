from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def count_operation(self, arr: list[int]) -> int:
        idx = 0
        arr_sorted = arr.copy()
        arr_sorted.sort()
        dic = { key: val for val, key in enumerate(arr_sorted) }
        ans = 0
        while idx < len(arr):
            real_idx = dic[arr[idx]]
            while real_idx != idx:
                ans += 1
                new_idx = dic[arr[real_idx]]
                arr[real_idx], arr[idx] = arr[idx], arr[real_idx]
                idx = new_idx
                real_idx = dic[arr[idx]]
            if real_idx == idx:
                idx += 1
        print(dic)
        return ans

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        ans = 0
        while len(q) > 0:
            arr_list = list(map(lambda x: x.val, q)).copy()
            op_cnt = self.count_operation(arr_list)
            print(list(map(lambda x: x.val, q)), op_cnt)
            ans += op_cnt
            new_q = deque()
            while len(q) > 0:
                node = q.popleft()
                if node.left is not None:
                    new_q.append(node.left)
                if node.right is not None:
                    new_q.append(node.right)
                # arr_list = list(map(lambda x: x.val, new_q))
                # print(arr_list)
            q = new_q
        return ans

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

# null = None
# tree_root = make_leetree([428,46,239,494,281,147,null,null,142,25,325,155,482,246,232,331,164,461,221,220,293,252,297,null,null,null,null,238,null,null,null,404,460,71,null,225,483,null,148,null,null,null,402,null,null,217,265,400,null,null,null,406,305,null,null,null,196,null,null,236,null,361,108,458,149,407,256,371,302,41,null,null,null,null,161,null,351,245,224,null,475,null,null,null,null,null,null,278,null,null,null,null,null,null,null,303,null,null,240,null,320,310,null,24,74,null,null,null,null,null,48,null,285,null,null,null,23,null,399])
# r = Solution().minimumOperations(tree_root)
# print(r)

test = [236, 361, 108, 458, 149, 407, 256, 371, 302, 41]
print(Solution().count_operation(test))
print(test)