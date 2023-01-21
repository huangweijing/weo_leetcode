class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        alp_grp = [set[str]([chr(ord("a") + _)]) for _ in range(26)]
        for i, ch1 in enumerate(s1):
            ch2 =s2[i]
            ch1_idx = ord(ch1) - ord("a")
            ch2_idx = ord(ch2) - ord("a")

            g1 = alp_grp[ch1_idx]
            g2 = alp_grp[ch2_idx]
            new_group = g1.union(g2)

            for ele in new_group:
                alp_grp[ord(ele) - ord("a")] = new_group

        min_dict = dict[str, str]()
        for i, s in enumerate(alp_grp):
            l = list(alp_grp[i])
            l.sort()
            min_dict[chr(ord("a") + i)] = l[0]

        ans = ""
        for ch in baseStr:
            ans += min_dict[ch]
        return ans

data = [
    "leetcode"
    , "programs"
    , "sourcecode"
]
r = Solution().smallestEquivalentString(* data)
print(r)

