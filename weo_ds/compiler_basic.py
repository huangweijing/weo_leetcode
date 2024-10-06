from collections import Counter


class Solution:
    def __init__(self):
        self.f = ""
        self.p = 0

    def get_word(self) -> Counter:
        res = Counter()
        chem, cnt = self.get_chem(), self.get_cnt()
        # print(chem, cnt)
        res[chem] = cnt
        return res

    def get_chem(self) -> str:
        res = ""
        if self.p < len(self.f) and self.f[self.p].isupper():
            res += self.f[self.p]
            self.p += 1
            while self.p < len(self.f) and self.f[self.p].islower():
                res += self.f[self.p]
                self.p += 1
            return res
        return res

    def get_cnt(self) -> int:
        cnt_str = ""
        while self.p < len(self.f) and "0" <= self.f[self.p] <= "9":
            cnt_str += self.f[self.p]
            self.p += 1
        if cnt_str == "":
            return 1
        return int(cnt_str)

    def get_group(self) -> Counter:
        res = Counter()
        if self.p < len(self.f) and self.f[self.p] == "(":
            self.p += 1
            formula = self.get_formula()
            self.p += 1
            cnt = self.get_cnt()
            for key, val in formula.items():
                res[key] = val * cnt
            return res
        else:
            return res

    def get_formula(self) -> Counter:
        res = Counter()
        while self.p < len(self.f) and self.f[self.p] != ")":
            if self.f[self.p] == "(":
                res += self.get_group()
            elif self.f[self.p].isupper():
                res += self.get_word()
            # print(res)
        return res

    def countOfAtoms(self, formula: str) -> str:
        self.p, self.f = 0, formula
        cnt = self.get_formula()
        ans = ""
        for k, v in sorted(cnt.items(), key=lambda x: x[0]):
            ans += k + (str(v) if v != 1 else "")
        return ans


r = Solution().countOfAtoms("H2O(H2O)2(Mg2CH3)3")
print(r)