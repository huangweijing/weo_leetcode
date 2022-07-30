class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch_dic = dict[str, str]()
        rv_ch_dic = dict[str, str]()
        for i, ch in enumerate(s):
            if ch not in ch_dic:
                ch_dic[ch] = t[i]
            else:
                if ch_dic[ch] != t[i]:
                    return False

            if t[i] not in rv_ch_dic:
                rv_ch_dic[t[i]] = ch
            else:
                if rv_ch_dic[t[i]] != ch:
                    return False
        return True
