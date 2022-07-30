class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polish_stack = []
        for token in tokens:
            if token == "*":
                n1 = polish_stack.pop()
                n2 = polish_stack.pop()
                polish_stack.append(n1 * n2)
            elif token == "+":
                n1 = polish_stack.pop()
                n2 = polish_stack.pop()
                polish_stack.append(n1 + n2)
            elif token == "-":
                n1 = polish_stack.pop()
                n2 = polish_stack.pop()
                polish_stack.append(n2 - n1)
            elif token == "/":
                n1 = polish_stack.pop()
                n2 = polish_stack.pop()
                polish_stack.append(int(n2 / n1))
            else:
                polish_stack.append(int(token))
        return polish_stack[0]