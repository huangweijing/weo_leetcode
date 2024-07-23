from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        cur = head
        new_head = head
        last = None
        while cur is not None:
            if cur.val in nums:
                if last is not None:
                    last.next = cur.next
                    cur = cur.next
                    continue
                else:
                    new_head = cur.next
                    last = None
                    cur = cur.next
                    continue
            else:
                last = cur
                cur = cur.next
        return new_head
        