from collections import deque


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [num for i, num in enumerate(nums) if i & 1 == 0]
        odd = [num for i, num in enumerate(nums) if i & 1 == 1]
        even.sort()
        odd.sort(reverse=True)
        q_even, q_odd = deque(even), deque(odd)
        ans = []
        while len(q_even) > 0 or len(q_odd) > 0:
            if len(q_even) > 0:
                ans.append(q_even.popleft())
            if len(q_odd) > 0:
                ans.append(q_odd.popleft())
        return ans

