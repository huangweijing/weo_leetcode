from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.arr = []

    def make_tree(self, start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None
        if start == end:
            return TreeNode(self.arr[start])
        mid = start + end >> 1
        return TreeNode(self.arr[mid]
                        , self.make_tree(start, mid - 1)
                        , self.make_tree(mid + 1, end))

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        node = head
        while node is not None:
            arr.append(node.val)
            node = node.next
        self.arr = arr
        return self.make_tree(0, len(arr) - 1)

