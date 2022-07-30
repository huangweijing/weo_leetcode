class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_stk = list[ListNode]()
        cur = head
        idx = 1
        while cur is not None:
            node_stk.append(cur)
            cur = cur.next
            idx += 1
        tmp_val = node_stk[k - 1].val
        node_stk[k - 1].val = node_stk[-k].val
        node_stk[-k].val = tmp_val
        return head