class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ps_dict = dict[str, str]()
        sp_dict = dict[str, str]()
        s_arr = s.split(sep=" ")
        if len(s_arr) != len(pattern):
            return False
        for i, ch in enumerate(pattern):
            if ch not in ps_dict:
                ps_dict[ch] = s_arr[i]
            else:
                if ps_dict[ch] != s_arr[i]:
                    return False

        for i, token in enumerate(s_arr):
            if token not in sp_dict:
                sp_dict[token] = pattern[i]
            else:
                if sp_dict[token] != pattern[i]:
                    return False
        return True
