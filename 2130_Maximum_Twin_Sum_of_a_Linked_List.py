from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node_arr = []
        cur = head
        while cur is not None:
            node_arr.append(cur.val)
            cur = cur.next
        result = 0
        # print(node_arr)
        for i in range((len(node_arr) >> 1)):
            result = max(result, node_arr[i] + node_arr[ - 1 - i])
        return result
