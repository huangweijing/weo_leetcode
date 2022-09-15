class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head is not None:
            result <<= 1
            result += head.val
            head = head.next
        return result
