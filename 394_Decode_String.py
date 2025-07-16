class Solution:
    def __init__(self) -> None:
        self.idx = 0
        self.s = ""

    def read_int(self):
        val = 0
        while self.idx < len(self.s) and "0" <= self.s[self.idx] <= "9":
            val = val * 10 + int(self.s[self.idx])
            self.idx += 1
        return val
        
    def read_alp(self):
        val = ""
        while self.idx < len(self.s) and "a" <= self.s[self.idx] <= "z":
            val = val + self.s[self.idx]
            self.idx += 1
        return val

    def read_bracket(self):
        if self.idx == len(self.s):
            return ""
        # print("bbbbaaa", self.idx)
        if self.s[self.idx] != "[":
            return ""
        self.idx += 1
        exp = self.read_exp()
        self.idx += 1
        return exp
        
    def read_exp(self):
        if self.idx == len(self.s):
            return ""
        if self.s[self.idx] in ("[", "]"):
            return ""
        val = ""
        cnt = self.read_int()
        bkt = self.read_bracket()
        val += bkt * cnt
        # print(cnt, bkt)
        val += self.read_alp()
        val += self.read_exp()
        return val

    def decodeString(self, s: str) -> str:
        self.s = s
        return self.read_exp()
    
data = "2[ab2[cc]]"
r = Solution().decodeString(data)
print(r)

        


        
            
        