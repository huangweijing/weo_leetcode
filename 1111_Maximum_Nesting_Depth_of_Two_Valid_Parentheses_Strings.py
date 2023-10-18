from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth_arr = []
        depth, max_depth = 0, 0
        stk = []
        for ch in seq:
            if ch == "(":
                stk.append(ch)
                depth += 1
                depth_arr.append(depth)
            else:
                stk.pop()
                depth_arr.append(depth)
                depth -= 1
            max_depth = max(depth, max_depth)
        return [ 0 if d <= max_depth // 2 else 1 for d in depth_arr]



