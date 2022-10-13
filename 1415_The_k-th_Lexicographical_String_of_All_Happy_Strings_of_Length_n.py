class Solution:
    def gen_str(self, n) -> list[str]:
        if n == 1:
            return ["a", "b", "c"]
        sub = self.gen_str(n - 1)
        result = []
        for s in sub:
            for post in ["a", "b", "c"]:
                if post == s[-1]:
                    continue
                result.append(s + post)
        return result

    def getHappyString(self, n: int, k: int) -> str:
        hs = self.gen_str(n)
        if len(hs) < k:
            return ""
        else:
            return hs[k - 1]

r = Solution().getHappyString(3, 9)
print(r)
