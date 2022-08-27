class Solution:
    def push_backspace(self, s: str) -> str:
        result = []
        for ch in s:
            if ch == "#":
                if len(result) > 0:
                    result.pop()
            else:
                result.append(ch)
        return "".join(result)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.push_backspace(s) == self.push_backspace(t)

