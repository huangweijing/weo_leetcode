class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_stack = []
        self.forward_stack = []
        self.current = homepage

    def visit(self, url: str) -> None:
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self, steps: int) -> str:
        while len(self.back_stack) > 0:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
            if steps == 0:
                break
        return self.current

    def forward(self, steps: int) -> str:
        while len(self.forward_stack) > 0:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1
            if steps == 0:
                break
        return self.current
