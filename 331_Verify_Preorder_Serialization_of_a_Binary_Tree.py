class Solution:
    def __init__(self):
        self.po_str = []
        self.res = True

    def validate(self, idx: int) -> int:
        if not self.res:
            return -1
        if idx >= len(self.po_str):
            self.res = False
            return -1
        # print(idx, self.po_str[idx])
        if self.po_str[idx] == "#":
            return idx + 1
        if idx + 2 >= len(self.po_str):
            self.res = False
            return -1
        idx += 1
        idx = self.validate(idx)
        idx = self.validate(idx)
        return idx

    def isValidSerialization(self, preorder: str) -> bool:
        self.po_str = preorder.split(",")
        idx = self.validate(0)
        if not self.res:
            return False
        if idx == len(self.po_str):
            return True
        return False

data = "1,#,#"
r = Solution().isValidSerialization(data)
print(r)