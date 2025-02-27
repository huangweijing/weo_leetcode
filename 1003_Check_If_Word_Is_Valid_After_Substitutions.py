class Solution:
    def __init__(self) -> None:
        self.idx = 0
        self.s = ""
        self.res = True

    def read_abc(self) -> bool:
        if self.idx == len(self.s):
            return True
        if self.s[self.idx] == "a":
            self.idx += 1
        else:
            return True
        ret = self.read_abc()
        if not ret or self.idx == len(self.s):
            return False
        if self.s[self.idx] == "b":
            self.idx += 1
        else:
            return False
        ret = self.read_abc()
        if not ret or self.idx == len(self.s):
            return False
        if self.s[self.idx] == "c":
            self.idx += 1
        else:
            return False
        ret = self.read_abc()
        if not ret:
            return False
        return True
        

    def isValid(self, s: str) -> bool:
        self.s = s
        while self.idx < len(s):
            old_idx = self.idx
            ret = self.read_abc()
            if not ret or old_idx == self.idx:
                return False
            # print(self.idx)
        return True
        
    
r = Solution().isValid("ababcabcc")
print(r)
            