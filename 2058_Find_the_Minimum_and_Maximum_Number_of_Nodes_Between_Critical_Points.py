from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idx = 0
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]
        cur, cur_next, cur_next_next = head, head.next, head.next.next
        ans = [math.inf, -1]
        min_idx, max_idx = math.inf, -math.inf
        last_idx = -1
        while cur is not None and cur_next is not None and cur_next_next is not None:
            if (cur_next.val > cur.val and cur_next.val > cur_next_next.val) \
                    or (cur_next.val < cur.val and cur_next.val < cur_next_next.val):
                min_idx = min(min_idx, idx)
                max_idx = max(max_idx, idx)
                if last_idx != -1:
                    ans[0] = min(ans[0], idx - last_idx)
                last_idx = idx
            idx += 1
            cur = cur_next
            cur_next = cur_next_next
            cur_next_next = cur_next_next.next
        if ans[0] == math.inf:
            ans[0] = -1
        if max_idx == -math.inf or max_idx == min_idx:
            ans[1] = -1
        else:
            ans[1] = max_idx - min_idx

        return ans

# data = [1,3,2,2,3,2,2,2,7]
# r = Solution().nodesBetweenCriticalPoints(data)
# print(r)