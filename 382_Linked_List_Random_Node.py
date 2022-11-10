import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        cur = head
        while cur is not None:
            self.arr.append(cur.val)
            cur = cur.next

    def getRandom(self) -> int:
        random_idx = random.Random().randint(0, len(self.arr)- 1)
        return self.arr[random_idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()