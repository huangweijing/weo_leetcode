class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        node_list = list[ListNode]()
        cur = head
        while cur is not None:
            node_list.append(cur)
            cur = cur.next

        new_head = node_list[-1]
        for i in range(len(node_list) - 1, 0, -1):
            node_list[i].next = node_list[i - 1]
        node_list[0].next = None
        return new_head

