from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        stk = []
        while cur is not None:
            stk.append(cur)
            cur = cur.next
        ans = []
        while k > 0:
            cnt = len(stk) // k
            arr = []
            while cnt > 0:
                arr.append(stk.pop())
                cnt -= 1
            if len(arr) > 0:
                arr[0].next = None
                ans.append(arr[-1])
            else:
                ans.append(None)
            k -= 1
        return ans[::-1]
