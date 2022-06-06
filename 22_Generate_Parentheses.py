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

    def generateParenthesis(self, n: int) -> list[str]:
        par_list = self.generateParenthesisTmp(n)
        result = []
        for par in par_list:
            if self.isValid(par):
                result.append(par)
        return result


    def generateParenthesisTmp(self, n: int) -> list[str]:

        if n == 1:
            return ["()", ")(", "))", "(("]

        result_n_1: list[str] = self.generateParenthesisTmp(n-1)
        result_n = set()
        for r in result_n_1:
            result_n.add(r + "()")
            result_n.add("()" + r)
            result_n.add("(" + r + ")")
            result_n.add(")" + r + "(")
            result_n.add(")(" + r)
            result_n.add(r + ")(")

            result_n.add(r + "))")
            result_n.add("))" + r)
            result_n.add(")" + r + ")")
            result_n.add("(" + r + "(")
            result_n.add("((" + r)
            result_n.add(r + "((")
        # print(list(result_n))
        return list(result_n)



sol = Solution()
s = sol.generateParenthesis(8)
print(s)



