from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        node_list = list[ListNode]()
        while cur is not None:
            node_list.append(cur)
            cur = cur.next
        last_node = None
        for i in range(int(len(node_list) / 2)):
            idx_from_back = len(node_list) - 1 - i
            node_list[i].next = node_list[idx_from_back]
            node_list[idx_from_back].next = node_list[i + 1]
            last_node = node_list[i + 1]

        if last_node is not None:
            last_node.next = None