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
        self.head = None
        self.ans = False

    def my_sol(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if head and not root:
            return False
        if head.val == root.val:
            return self.my_sol(head.next, root.left) or self.my_sol(head.next, root.right)
        return False

    def my_sol2(self, root: Optional[TreeNode]):
        if not root:
            return False
        if self.my_sol(self.head, root):
            print(f"matched {root.val}!")
            self.ans = root.val
            return True
        self.my_sol2(root.left) or self.my_sol2(root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        self.head = head
        self.my_sol2(root)
        return self.ans

