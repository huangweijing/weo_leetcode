from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        node_list = list[int]()
        while cur:
            node_list.append(cur.val)
            cur = cur.next

        for i in range(len(node_list) >> 1):
            if node_list[i] != node_list[-1 - i]:
                return False
        return True
