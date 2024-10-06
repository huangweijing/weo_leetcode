from typing import List
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        open_cnt, close_cnt, close_arr = 0, 0, deque()
        trouble_close_arr, trouble_open_arr = deque(), deque()
        for i, ch in enumerate(s):
            if ch == "(":
                open_cnt += 1
            elif ch == ")":
                close_cnt += 1
                close_arr.append(i)
                if close_cnt > open_cnt:
                    trouble_close_arr.append(close_arr.copy())
                    close_cnt -= 1
        open_cnt, close_cnt, close_arr = 0, 0, deque()
        for i, ch in enumerate(reversed(s)):
            if ch == ")":
                open_cnt += 1
            elif ch == "(":
                close_cnt += 1
                close_arr.appendleft(len(s) - 1- i)
                if close_cnt > open_cnt:
                    trouble_open_arr.appendleft(close_arr.copy())
                    close_cnt -= 1
        # print(trouble_open_arr, trouble_close_arr)
        pattern = set[int]([0])
        for trouble in trouble_open_arr:
            new_patthern = set[int]()
            for p in pattern:
                for t in trouble:
                    if (1 << t) & p == 0:
                        new_patthern.add(p | (1 << t))
            pattern = new_patthern
        for trouble in trouble_close_arr:
            new_patthern = set[int]()
            for p in pattern:
                for t in trouble:
                    if (1 << t) & p == 0:
                        new_patthern.add(p | (1 << t))
            pattern = new_patthern
        # print(list(map(lambda x: bin(x), pattern)))

        ans = set()
        for p in pattern:
            res = ""
            for i, ch in enumerate(s):
                if p & (1 << i) == 0:
                    res += ch
            ans.add(res)
        # print(ans)
        return list(ans)


data = "(a)())()"
r = Solution().removeInvalidParentheses(data)
print(r)

