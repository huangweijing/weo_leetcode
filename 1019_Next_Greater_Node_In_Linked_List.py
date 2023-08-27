from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        idx, ans = 0, []
        stk = []
        while cur is not None:
            ans.append(0)
            while len(stk) > 0 and cur.val > stk[-1][1]:
                stk_item = stk.pop()
                ans[stk_item[0]] = cur.val
            stk.append([idx, cur.val])
            idx += 1
            cur = cur.next
        return ans