from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left -= 1
        right -= 1
        node_arr = list[ListNode]()
        cur = head
        while cur is not None:
            node_arr.append(cur)
            cur = cur.next

        while left < right:
            right_node = node_arr[right]
            node_arr[right] = node_arr[left]
            node_arr[left] = right_node
            left += 1
            right -= 1

        for i in range(len(node_arr) - 1):
            node_arr[i].next = node_arr[i + 1]

        node_arr[-1].next = None
        return node_arr[0]



