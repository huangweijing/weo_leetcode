from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        need_check = True
        while need_check:
            sum_val = 0
            sum_dict = dict[int, Optional[ListNode]]()
            sum_dict[0] = None
            cur = head
            need_check = False
            while cur is not None:
                sum_val += cur.val
                if sum_val in sum_dict:
                    tmp = sum_dict[sum_val]
                    if tmp is None:
                        head = cur.next
                    else:
                        tmp.next = cur.next
                    need_check = True
                    break
                sum_dict[sum_val] = cur
                cur = cur.next
        return head



def build_from_list(data: list[int]):
    head = ListNode()
    head.val = data[0]
    last = head
    for num in data[1:]:
        node = ListNode()
        node.val = num
        last.next = node
        last = node
    return head

def print_list(head: ListNode):
    cur = head
    arr = []
    while cur:
        arr.append(cur.val)
        cur = cur.next
    print(arr)

ln = build_from_list([2,6,1,-7,-1,8])
# print_list(ln)
r = Solution().removeZeroSumSublists(ln)
print_list(r)