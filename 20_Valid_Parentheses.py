class Solution:
    def isValid(self, s: str) -> bool:
        par_stack = list()
        for ch in s:
            if ch in ["[", "{", "("]:
                par_stack.append(ch)
            else:
                if len(par_stack) == 0:
                    return False
                par = par_stack.pop()
                if not (
                        (par == "(" and ch == ")") or
                        (par == "{" and ch == "}") or
                        (par == "[" and ch == "]")):
                    return False
        if len(par_stack) == 0:
            return True
        else:
            return False

sol = Solution()
r = sol.isValid("()[]{[}")
print(r)