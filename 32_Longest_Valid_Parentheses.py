class Solution:
    def longestValidParentheses(self, s: str) -> int:
        par_stack = list[str]()
        longest_size = 0
        current_size = 0
        last_open_idx: int = None
        for i, ch in enumerate(s):
            # print(par_stack, current_size)
            if ch == "(":
                if last_open_idx is None:
                    par_stack.append(i)
                else:
                    par_stack.append(last_open_idx)
                    last_open_idx = None
            else:
                if len(par_stack) > 0:
                    open_idx = par_stack.pop()
                else:
                    last_open_idx = None
                    continue

                current_size = i - open_idx + 1
                if current_size > longest_size:
                    longest_size = current_size
                if i + 1 < len(s) and s[i + 1] == "(":
                    last_open_idx = open_idx
                else:
                    last_open_idx = None
        return longest_size

sol = Solution()
r = sol.longestValidParentheses(")()())")
print(r)







